from __future__ import annotations

import abc
import enum
import typing as t
from abc import abstractmethod
from dataclasses import dataclass

import click
import pytermor as pt


# -----------------------------------------------------------------------------
# Parameter types


class IntRange(click.IntRange):
    def __init__(
        self,
        _min: t.Optional[float] = None,
        _max: t.Optional[float] = None,
        min_open: bool = False,
        max_open: bool = False,
        clamp: bool = False,
        show_range: bool = True,
    ):
        self._show_range = show_range
        super().__init__(_min, _max, min_open, max_open, clamp)

    def get_metavar(self, param: click.Parameter = None) -> t.Optional[str]:
        return "N"

    def _describe_range(self) -> str:
        if not self._show_range:
            return ""
        return super()._describe_range().replace("x", self.get_metavar())


class FloatRange(click.FloatRange):
    def __init__(
        self,
        _min: t.Optional[float] = None,
        _max: t.Optional[float] = None,
        min_open: bool = False,
        max_open: bool = False,
        clamp: bool = False,
        show_range: bool = True,
    ):
        self._show_range = show_range
        super().__init__(_min, _max, min_open, max_open, clamp)

    def get_metavar(self, param: click.Parameter = None) -> t.Optional[str]:
        return "X"

    def _describe_range(self) -> str:
        if not self._show_range:
            return ""
        return super()._describe_range().replace("x", self.get_metavar())


class EnumChoice(click.Choice):
    """
    Note: `show_choices` is ignored if param has custom metavar. That's because
    both metavar and choices in the left column of parameter list in --help mode
    look like shit and mess up the whole table. In case you need to set a metavar
    and to display choices at the same, insadd the latter into "help" message
    manually (see `exec_notify.NotifyCommand`).
    """

    def __init__(self, impl: t.Any | enum.Enum, show_choices=True):
        self.__impl = impl
        self._show_choices = show_choices
        super().__init__(choices=[item.value for item in impl], case_sensitive=False)

    def get_metavar(self, param: click.Parameter) -> str:
        if not self._show_choices:
            return ""
        return super().get_metavar(param)

    def convert(self, value, param, ctx):
        if value is None or isinstance(value, enum.Enum):
            return value

        converted_str = super().convert(value, param, ctx)
        return self.__impl(converted_str)


class OptionScope(str, enum.Enum):
    COMMON = "Common options"
    GROUP = "Group options"
    COMMAND = "Options"

    def __str__(self):
        return self.value


# -----------------------------------------------------------------------------
# Command options

class ScopedOption(click.Option, metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def scope(self) -> OptionScope:
        raise NotImplementedError

    def has_argument(self):
        if isinstance(self.type, click.IntRange):
            return not self.count
        return isinstance(
            self.type,
            (
                click.FloatRange,
                click.Choice,
                click.DateTime,
            ),
        )


class CommonOption(ScopedOption):
    scope = OptionScope.COMMON


class GroupOption(ScopedOption):
    scope = OptionScope.GROUP


class CommandOption(ScopedOption):
    scope = OptionScope.COMMAND


class DayMonthOption(CommandOption):
    _date_formats = ["%b-%d", "%m-%d", "%d-%b", "%d-%b", "%b%d", "%m%d", "%d%b", "%d%m"]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("type", click.DateTime(self._date_formats))
        kwargs.setdefault("show_default", "current")
        kwargs.setdefault("metavar", "DD-MM")
        kwargs.setdefault(
            "help",
            "Date of interest, where DD is a number between 1 and 31, and MM is "
            "either a number between 1 and 12 or month short name (first 3 characters). "
            "MM-DD format is also accepted. Hyphen can be omitted.",
        )
        super().__init__(*args, **kwargs)


# -----------------------------------------------------------------------------
# Command epilogues


@dataclass()
class EpilogPart:
    text: str
    title: str = None
    group: str = None


EPILOG_COMMAND_HELP = EpilogPart(
    "Run '%s' 'COMMAND' '--help' to get the COMMAND usage details (e.g. '%s' '%s' '--help').",
    group="run",
)
EPILOG_COMMON_OPTIONS = EpilogPart(
    "Run 'es7s options' to see common options details ('-v', '-q', '-c', '-C', '--tmux', "
    "'--default').",
    group="run",
)
EPILOG_ARGS_NOTE = EpilogPart(
    "Mandatory or optional arguments to long options are also mandatory or optional for any "
    "corresponding short options."
)


# -----------------------------------------------------------------------------
# Command types

@dataclass
class CommandType:
    char: str | None
    name: str
    sorter: int
    fmt: pt.FT = pt.NOOP_STYLE
    description: str = None

    def __hash__(self) -> int:
        return hash(f'{self.char or ""}{self.name}{self.fmt!r}')


CMDTYPE_DEFAULT = CommandType(
    None,
    "regular command",
    sorter=0,
)
CMDTYPE_GROUP = CommandType(
    "+",
    "command group",
    sorter=10,
    fmt=pt.cv.HI_BLUE,
)
CMDTYPE_EXTERNAL = CommandType(
    "^",
    "standalone component",
    sorter=20,
    fmt=pt.cv.BLUE,
    description="this is a standalone component which can be launched directly",
)
CMDTYPE_X11 = CommandType(
    "*",
    "X11 component",
    sorter=30,
    fmt=pt.cv.MAGENTA,
    description="this command works in X11 (GUI) environment only",
)
CMDTYPE_DYNAMIC = CommandType(
    "~",
    "adaptive",
    sorter=40,
    fmt=pt.cv.GREEN,
    description="this command adjusts the output format depending on terminal configuration",
)
