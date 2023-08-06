from __future__ import annotations

import functools as ft
import sys
from collections.abc import MutableMapping, MutableSequence
from contextlib import suppress
from types import FunctionType, MappingProxyType
from typing import Any, Callable, NamedTuple, Sequence, TypeVar

import jax.tree_util as jtu
from typing_extensions import dataclass_transform

from pytreeclass._src.tree_freeze import tree_hash
from pytreeclass._src.tree_indexer import (
    _conditional_mutable_method,
    _leafwise_transform,
    _mutable_context,
    is_tree_equal,
    tree_copy,
    tree_indexer,
)
from pytreeclass._src.tree_pprint import tree_repr, tree_str
from pytreeclass._src.tree_trace import register_pytree_node_trace


class NOT_SET:
    __repr__ = lambda _: "?"


PyTree = Any
T = TypeVar("T")
_NOT_SET = NOT_SET()
_FIELDS = "__fields__"
_POST_INIT = "__post_init__"
_MUTABLE_TYPES = (MutableSequence, MutableMapping, set)


"""Define a class decorator that is compatible with JAX's transformation."""


def is_treeclass(node: Any) -> bool:
    """Check if a node is a `treeclass`."""
    return (node if isinstance(node, type) else type(node)).__setattr__ is _setattr


class Field(NamedTuple):
    name: str | None = None
    type: type | None = None
    default: Any = _NOT_SET
    factory: Any = None
    init: bool = True
    repr: bool = True
    kw_only: bool = False
    pos_only: bool = False
    metadata: MappingProxyType[str, Any] | None = None
    callbacks: Sequence[Any] = ()
    alias: str | None = None

    def __eq__(self, other: Any) -> bool:
        return hash(self) == hash(other)

    def __repr__(self) -> str:
        return tree_repr(self)

    def __hash__(self) -> int:
        parameters = (
            self.name,
            self.default,
            self.factory,
            self.init,
            self.kw_only,
            self.pos_only,
            self.alias,
        )
        return tree_hash(parameters)


def field(
    *,
    default: Any = _NOT_SET,
    factory: Callable | None = None,
    init: bool = True,
    repr: bool = True,
    kw_only: bool = False,
    pos_only: bool = False,
    metadata: dict[str, Any] | None = None,  # type: ignore
    callbacks: Sequence[Any] = (),
    alias: str | None = None,
) -> Field:
    """
    Args:
        default: The default value of the field. Mutually exclusive with `factory`.
        factory: A 0-argument function called to initialize field value. Mutually exclusive with `default`.
        init: Whether the field is included in the object's __init__ function.
        repr: Whether the field is included in the object's __repr__ function.
        kw_only: Whether the field is keyword-only. Mutually exclusive with `pos_only`.
        pos_only: Whether the field is positional-only. Mutually exclusive with `kw_only`.
        metadata: A mapping of user-defined data for the field.
        callbacks: A sequence of functions to called on `setattr` during initialization to modify the field value.
        alias: An a alias for the field name in the constructor.

    Example:
        >>> import pytreeclass as pytc
        >>> def instance_cb_factory(klass):
        ...    def wrapper(x):
        ...        assert isinstance(x, klass)
        ...        return x
        ...    return wrapper


        >>> def positive_check_callback(x):
        ...    assert x > 0
        ...    return x

        >>> @pytc.treeclass
        ... class Employee:
        ...    # assert employee `name` is str
        ...    name: str = pytc.field(callbacks=[instance_cb_factory(str)])
        ...    # use callback compostion to assert employee `age` is int and positive
        ...    age: int = pytc.field(callbacks=[instance_cb_factory(int), positive_check_callback])
        ...    # use `id` in the constructor for `_id` attribute
        ...    # this is useful for private attributes that are not supposed to be accessed directly
        ...    # and hide it from the repr, also add extra info for this field
        ...    _id: int = pytc.field(alias="id", repr=False)

        >>> tree = Employee(name="Asem", age=10, id=1)
        >>> print(tree)  # _id is not shown
        Employee(name=Asem, age=10)
        >>> assert tree._id == 1  # this is the private attribute
    """
    if not isinstance(alias, (str, type(None))):
        msg = "`alias` must be a string or None, "
        msg += f"got type=`{type(alias).__name__}` instead."
        raise TypeError(msg)

    if default is not _NOT_SET and factory is not None:
        msg = "`default` and `factory` are mutually exclusive arguments."
        msg += f"got default={default} and factory={factory}"
        raise ValueError(msg)

    if kw_only is True and pos_only is True:
        msg = "`kw_only` and `pos_only` are mutually exclusive arguments."
        msg += f"got kw_only={kw_only} and pos_only={pos_only}"
        raise ValueError(msg)

    if isinstance(metadata, dict):
        metadata = MappingProxyType(metadata)  # type: ignore
    elif metadata is not None:
        raise TypeError("`metadata` must be a Mapping or None")

    if not isinstance(callbacks, Sequence):
        msg = f"`callbacks` must be a Sequence of functions, got {type(callbacks)}"
        raise TypeError(msg)

    for index, callback in enumerate(callbacks):
        if not isinstance(callback, Callable):  # type: ignore
            msg = "`callbacks` must be a Sequence of functions, "
            msg += f"got `{type(callbacks).__name__}` at index={index}"
            raise TypeError(msg)

    return Field(
        name=None,
        type=None,
        default=default,
        factory=factory,
        init=init,
        repr=repr,
        kw_only=kw_only,
        pos_only=pos_only,
        metadata=metadata,  # type: ignore
        callbacks=callbacks,
        alias=alias,
    )


def fields(item: Any) -> Sequence[Field]:
    """Get the fields of a `treeclass` instance."""
    if not hasattr(item, _FIELDS):
        raise TypeError(f"Cannot get fields of {item!r}.")

    return tuple(vars(item)[_FIELDS].values())


@ft.lru_cache
def _generate_field_map(klass: type) -> dict[str, Field]:
    field_map = dict()

    if klass is object:
        return field_map

    for base in reversed(klass.__mro__[1:]):
        # get the fields of the base class in the MRO in reverse order to ensure
        # the correct order of the fields are preserved
        field_map.update(_generate_field_map(base))

    # TODO: use inspect to get annotations, once we are on minimum python version >3.9
    if "__annotations__" not in vars(klass):
        return field_map

    for name in (annotation_map := vars(klass)["__annotations__"]):
        value = vars(klass).get(name, _NOT_SET)
        type = annotation_map[name]

        if name == "self":
            # while `dataclasses` allows `self` as a field name, its confusing
            # and not recommended. so raise an error
            msg = "Field name cannot be `self`."
            raise ValueError(msg)

        if isinstance(value, Field):
            # case: `x: Any = field(default=1)`
            if isinstance(value.default, _MUTABLE_TYPES):
                # example case: `x: Any = field(default=[1, 2, 3])`
                msg = f"Mutable default value of field `{name}` is not allowed, use "
                msg += f"`factory=lambda: {value.default}` instead."
                raise TypeError(msg)

            field_map[name] = value._replace(name=name, type=type)

        elif isinstance(value, _MUTABLE_TYPES):
            # https://github.com/ericvsmith/dataclasses/issues/3
            # example case: `x: Any = [1, 2, 3]`
            msg = f"Mutable value= {(value)} is not allowed"
            msg += f" for field `{name}` in class `{klass.__name__}`.\n"
            msg += f" use `field(... ,factory=lambda:{value})` instead"
            raise TypeError(msg)

        elif value is _NOT_SET:
            # case: `x: Any`
            field_map[name] = Field(name=name, type=type)

        else:
            # case: `x: int = 1`
            field_map[name] = Field(name=name, type=type, default=value)

    return field_map


@ft.lru_cache
def _generate_init_code(fields: Sequence[Field]) -> str:
    head = body = ""

    for field in fields:
        name = field.name  # name in body
        alias = field.alias or name  # name in constructor

        mark0 = f"field_map['{name}'].default"
        mark1 = f"field_map['{name}'].factory()"
        mark2 = f"self.{name}"

        if field.kw_only and "*" not in head and field.init:
            head += "*, "

        if field.default is not _NOT_SET:
            # in head: def f(.. x= default_value)
            head += f"{alias}={mark0}, " if field.init else ""
            # in body:  self.x = default_value
            body += f"\t\t{mark2}=" + (f"{alias}\n " if field.init else f"{mark0}\n")
        elif field.factory is not None:
            head += f"{alias}={mark1}, " if field.init else ""
            body += f"\t\t{mark2}=" + (f"{alias}\n" if field.init else f"{mark1}\n")
        else:
            # no defaults are added
            head += f"{alias}, " if field.init else ""
            body += f"\t\t{mark2}={alias}\n " if field.init else ""

        if field.pos_only and field.init:
            if "/" in head:
                head = head.replace("/,", "")

            head += "/, "

    # add pass to avoid syntax error if all fields are ignored
    body += "\t\tpass"
    body = "\tdef __init__(self, " + head[:-2] + "):\n" + body
    body = f"def closure(field_map):\n{body}\n\treturn __init__"
    return body.expandtabs(4)


def _generate_init(klass: type) -> FunctionType:
    field_map = _generate_field_map(klass)
    local_namespace = dict()  # type: ignore
    global_namespace = vars(sys.modules[klass.__module__])
    init_code = _generate_init_code(tuple(field_map.values()))
    exec(init_code, global_namespace, local_namespace)
    method = local_namespace["closure"](field_map)

    return FunctionType(
        code=method.__code__,
        globals=global_namespace,
        name=method.__name__,
        argdefs=method.__defaults__,
        closure=method.__closure__,
    )


@_conditional_mutable_method
def _setattr(tree: PyTree, key: str, value: Any) -> None:
    if key in (field_map := vars(tree)[_FIELDS]):
        for callback in field_map[key].callbacks:
            try:
                # callback is a function that takes the value of the field
                # and returns a modified value
                value = callback(value)
            except Exception as e:
                msg = f"Error for field=`{key}`:\n{e}"
                raise type(e)(msg)

    if is_treeclass(value):
        # auto registers the instance value if it is a registered `treeclass`
        # this behavior is similar to PyTorch behavior in `nn.Module`
        # with instances of `Parameter`/`Module`.
        # the behavior is useful to avoid repetitive code pattern in field definition and
        # and initialization inside init method.
        kv = {key: Field(type=type(value), init=False, name=key)}
        vars(tree)[_FIELDS] = MappingProxyType({**vars(tree)[_FIELDS], **kv})

    vars(tree)[key] = value  # type: ignore


@_conditional_mutable_method
def _delattr(tree, key: str) -> None:
    # delete the attribute under `_mutable_context` context
    # otherwise raise an error
    del vars(tree)[key]


def _init_wrapper(init_func: Callable) -> Callable:
    @ft.wraps(init_func)
    def wrapper(tree, *a, **k) -> None:
        with _mutable_context(tree):
            kvs = dict(_generate_field_map(type(tree)))
            vars(tree)[_FIELDS] = MappingProxyType(kvs)
            output = init_func(tree, *a, **k)

            if post_init_func := getattr(type(tree), _POST_INIT, None):
                # to simplify the logic, we call the post init method
                # even if the init method is not code-generated.
                post_init_func(tree)

        # handle non-initialized fields
        if len(keys := set(kvs) - set(vars(tree))) > 0:
            msg = f"Uninitialized fields: ({', '.join(keys)}) "
            msg += f"in class `{type(tree).__name__}`"
            raise AttributeError(msg)
        return output

    return wrapper


def _tree_unflatten(klass: type, treedef: Any, leaves: list[Any]):
    tree = object.__new__(klass)
    # update through vars, to avoid calling the `setattr` method
    # that will check for callbacks.
    vars(tree).update(treedef[1])
    vars(tree).update(zip(treedef[0], leaves))
    return tree


def _tree_flatten(tree: PyTree):
    # Flatten rule for `treeclass` to use with `jax.tree_flatten`
    static, dynamic = dict(vars(tree)), dict()
    for key in static[_FIELDS]:
        dynamic[key] = static.pop(key)
    return list(dynamic.values()), (tuple(dynamic.keys()), static)


def _tree_trace(tree: PyTree) -> list[tuple[Any, Any, Any, Any]]:
    # Trace flatten rule to be used with the `tree_trace` module
    leaves, (keys, _) = _tree_flatten(tree)
    names = (f"{key}" for key in keys)
    types = map(type, leaves)
    indices = range(len(leaves))
    return [*zip(names, types, indices)]


def _register_treeclass(klass: type[T]) -> type[T]:
    with suppress(ValueError):
        # `ValueError` is raised for duplicate registration.
        # there are two cases where a class is registered more than once:
        # first, when a class is decorated with `treeclass` more than once (e.g. `treeclass(treeclass(Class))`)
        # second when a class is decorated with `treeclass` and has a parent class that is decorated with `treeclass`
        # in that case `__init_subclass__` registers the class before the decorator registers it.
        # register the trace flatten rule
        register_pytree_node_trace(klass, _tree_trace)
        # register the flatten/unflatten rules with jax
        jtu.register_pytree_node(klass, _tree_flatten, ft.partial(_tree_unflatten, klass))  # type: ignore

    return klass


def _init_subclass_wrapper(init_subclass_method: Callable) -> Callable:
    # Non-decorated subclasses uses the base `treeclass` leaves only
    @classmethod  # type: ignore
    @ft.wraps(init_subclass_method)
    def wrapper(klass: type, *a, **k) -> None:
        init_subclass_method(*a, **k)
        _register_treeclass(klass)

    return wrapper


def _treeclass_transform(klass: type[T]) -> type[T]:
    for key, method in (("__setattr__", _setattr), ("__delattr__", _delattr)):
        # basic required methods
        if key in vars(klass):
            if vars(klass)[key] is method:
                return klass  # already transformed
            # the user defined a method that conflicts with the required method
            msg = f"Unable to transform the class `{klass.__name__}` with {key} method defined."
            raise TypeError(msg)
        setattr(klass, key, method)

    if "__init__" not in vars(klass):
        # generate the init method in case it is not defined by the user
        setattr(klass, "__init__", _generate_init(klass))

    for key, wrapper in (
        ("__init__", _init_wrapper),
        ("__init_subclass__", _init_subclass_wrapper),
    ):
        # wrappers to enable the field initialization, and registering
        # the class with jax
        setattr(klass, key, wrapper(getattr(klass, key)))

    # basic optional methods
    for key, method in (
        ("__repr__", tree_repr),
        ("__str__", tree_str),
        ("__copy__", tree_copy),
        ("__hash__", tree_hash),
        ("__eq__", is_tree_equal),
        ("at", property(tree_indexer)),
    ):
        if key not in vars(klass):
            # keep the original method if it is defined by the user
            # this behavior similar is to `dataclasses.dataclass`
            setattr(klass, key, method)

    return klass


@dataclass_transform(field_specifiers=(field, Field), frozen_default=True)
def treeclass(klass: type[T], *, leafwise: bool = False) -> type[T]:
    """Convert a class to a JAX compatible tree structure.

    Args:
        klass: class to be converted to a `treeclass`
        leafwise: Wether to generate leafwise math operations methods. Defaults to `False`.

    Example:
        >>> import functools as ft
        >>> import jax
        >>> import pytreeclass as pytc

        >>> # Tree leaves are defined by type hinted fields at the class level
        >>> @pytc.treeclass
        ... class Tree:
        ...     a:int = 1
        ...     b:float = 2.0
        >>> tree = Tree()
        >>> jax.tree_util.tree_leaves(tree)
        [1, 2.0]

        >>> # Leaf-wise math operations are supported by setting `leafwise=True`
        >>> @ft.partial(pytc.treeclass, leafwise=True)
        ... class Tree:
        ...     a:int = 1
        ...     b:float = 2.0
        >>> tree = Tree()
        >>> tree + 1
        Tree(a=2, b=3.0)

        >>> # Advanced indexing is supported using `at` property
        >>> @pytc.treeclass
        ... class Tree:
        ...     a:int = 1
        ...     b:float = 2.0
        >>> tree = Tree()
        >>> tree.at[0].get()
        Tree(a=1, b=None)
        >>> tree.at["a"].get()
        Tree(a=1, b=None)

    Note:
        Indexing is supported for {`list`, `tuple`, `dict`, `defaultdict`, `OrderedDict`, `namedtuple`}
        and `treeclass` wrapped classes.

        Extending indexing to other types is possible by registering the type with
        `pytreeclass.register_pytree_node_trace`

    Note:
        `leafwise`=True adds the following methods to the class:
        .. code-block:: python
            '__add__', '__and__', '__ceil__', '__divmod__', '__eq__', '__floor__', '__floordiv__',
            '__ge__', '__gt__', '__invert__', '__le__', '__lshift__', '__lt__',
            '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__or__', '__pos__',
            '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__rfloordiv__',
            '__rlshift__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__',
            '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__sub__',
            '__truediv__', '__trunc__', '__xor__',

    Raises:
        TypeError: if the input is not a class.
    """
    klass = _register_treeclass(klass)
    # add math operations methods if leafwise
    # do not override any user defined methods
    klass = _leafwise_transform(klass) if leafwise else klass
    # add `repr`,'str', 'at', 'copy', 'hash', 'copy'
    # add the immutable setters and deleters
    # generate the `__init__` method if not present using type hints.
    klass = _treeclass_transform(klass)

    return klass
