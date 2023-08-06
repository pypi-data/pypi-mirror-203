from __future__ import annotations

import typing
from warnings import warn

from pyiron_contrib.workflow.has_to_dict import HasToDict
from pyiron_contrib.workflow.type_hinting import (
    valid_value, type_hint_is_as_or_more_specific_than
)

if typing.TYPE_CHECKING:
    from pyiron_contrib.workflow.node import Node


class Channel(HasToDict):
    """
    Channels control the flow of data on the graph.
    They have a label and belong to a node.
    They may optionally have a type hint.
    They may optionally have a storage priority (but this doesn't do anything yet).
    (In the future they may optionally have an ontological type.)

    Input/output channels can be (dis)connected from other output/input channels, and
    store all of their current connections in a list.

    The `value` held by a channel can be manually assigned, but should normally be set
    by the `update` method.
    In neither case is the type hint strictly enforced.
    Input channels will then propagate their value along to their owning node.
    Output channels with then propagate their value to all the input channels they're
    connected to.

    Type hinting is strictly enforced in one situation: when making connections to
    other channels and at least one channel has a non-None value for its type hint.
    In this case, we insist that the output type hint be _as or more more specific_ than
    the input type hint, to ensure that the input always receives output of a type it
    expects. This behaviour can be disabled and all connections allowed by setting
    `strict_connections = False` on the relevant input channel.

    For simple type hints like `int` or `str`, type hint comparison is trivial.
    However, some hints take arguments, e.g. `dict[str, int]` to specify key and value
    types; `tuple[int, int, str]` to specify a tuple with certain values;
    `typing.Literal['a', 'b', 'c']` to specify particular choices;
    `typing.Callable[[float, float], str]` to specify a callable that takes particular
    argument types and has a return type; etc.
    For hints with the origin `dict`, `tuple`, and `typing.Callable`, the two hints must
    have _exactly the same arguments_ for one two qualify as "as or more specific".
    E.g. `tuple[int, int|float]` is as or more specific than
    `tuple[int|float, int|float]`, but not `tuple[int, int|float, str]`.
    For _all other hints_, we demand that the output hint arguments be a _subset_ of
    the input.
    E.g. `Literal[1, 2]` is as or more specific that both `Literal[1, 2]` and
    `Literal[1, 2, "three"]`.

    Warning:
        Type hinting in python is quite complex, and determining when a hint is
        "more specific" can be tricky. For instance, in python 3.11 you can now type
        hint a tuple with a mixture of fixed elements of fixed type, followed by an
        arbitrary elements of arbitrary type. This and other complex scenarios are not
        yet included in our test suite and behaviour is not guaranteed.

    TODO:
        In direct relation to the above warning, it may be nice to add a flag to
        channels to turn on/off the strict enforcement of type hints when making
        connections.
    """
    def __init__(
            self,
            label: str,
            node: Node,
            default: typing.Optional[typing.Any] = None,
            type_hint: typing.Optional[typing.Any] = None,
            storage_priority: int = 0,
            strict_connections: bool = True,
    ):
        self.label = label
        self.node = node
        self.default = default
        self.value = default
        self.type_hint = type_hint
        self.storage_priority = storage_priority
        self.strict_connections = True
        self.connections = []

    @property
    def ready(self):
        if self.type_hint is not None:
            return valid_value(self.value, self.type_hint)
        else:
            return True

    def connect(self, *others: Channel):
        for other in others:
            if self._valid_connection(other):
                self.connections.append(other)
                other.connections.append(self)
                out, inp = self._figure_out_who_is_who(other)
                inp.update(out.value)
            else:
                if isinstance(other, Channel):
                    warn(
                        f"{self.label} ({self.__class__.__name__}) and {other.label} "
                        f"({other.__class__.__name__}) were not a valid connection"
                    )
                else:
                    raise TypeError(
                        f"Can only connect two channels, but {self.label} "
                        f"({self.__class__.__name__}) got a {other} ({type(other)})"
                    )

    def _valid_connection(self, other):
        if self._is_IO_pair(other) and not self._already_connected(other):
            if self._both_typed(other):
                out, inp = self._figure_out_who_is_who(other)
                if not inp.strict_connections:
                    return True
                else:
                    return type_hint_is_as_or_more_specific_than(
                        out.type_hint, inp.type_hint
                    )
            else:
                # If either is untyped, don't do type checking
                return True
        else:
            return False

    def _is_IO_pair(self, other: Channel):
        return isinstance(other, Channel) and type(self) != type(other)

    def _already_connected(self, other: Channel):
        return other in self.connections

    def _both_typed(self, other: Channel):
        return self.type_hint is not None and other.type_hint is not None

    def _figure_out_who_is_who(self, other: Channel) -> (OutputChannel, InputChannel):
        return (self, other) if isinstance(self, OutputChannel) else (other, self)

    def disconnect(self, *others: Channel):
        for other in others:
            if other in self.connections:
                self.connections.remove(other)
                other.disconnect(self)

    def disconnect_all(self):
        self.disconnect(*self.connections)

    @property
    def connected(self):
        return len(self.connections) > 0

    def __iter__(self):
        return self.connections.__iter__()

    def __len__(self):
        return len(self.connections)

    def __str__(self):
        return str(self.value)

    def to_dict(self):
        return {
            "label": self.label,
            "value": str(self.value),
            "ready": self.ready,
            "connected": self.connected,
            "connections": [f"{c.node.label}.{c.label}" for c in self.connections]
        }


class InputChannel(Channel):
    def update(self, value):
        self.value = value
        self.node.update()

    def activate_strict_connections(self):
        self.strict_connections = True

    def deactivate_strict_connections(self):
        self.strict_connections = False


class OutputChannel(Channel):
    def update(self, value):
        self.value = value
        for inp in self.connections:
            inp.update(self.value)
