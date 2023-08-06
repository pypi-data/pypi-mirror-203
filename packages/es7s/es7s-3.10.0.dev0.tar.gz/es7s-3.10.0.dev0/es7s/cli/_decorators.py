# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

from __future__ import annotations

import sys
import typing as t
from functools import update_wrapper

import click
from click import Argument
from click.decorators import F, FC, _param_memo

from ._base import CliGroup, CliCommand
from ._base_opts_params import EpilogPart, CommandOption, CMDTYPE_DEFAULT, CommandType
from ..shared import get_logger, get_stdout
from ..shared.threads import exit_gracefully


def _catch_and_log_and_exit(func: F) -> F:
    def wrapper(*args, **kwargs):
        logger = get_logger()
        try:
            logger.debug("Starting command execution")
            func(*args, **kwargs)
        except Exception as e:
            logger.exception(e)
            exit_gracefully(1)
        logger.debug("Command executed")
        return func

    return update_wrapper(t.cast(F, wrapper), func)


def _catch_and_print(func: F) -> F:
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            if stdout := get_stdout(require=False):
                stdout.echo("ERROR")
            else:
                sys.stdout.write("ERROR\n")
            raise
        return func

    return update_wrapper(t.cast(F, wrapper), func)


def cli_group(
    name: str,
    short_help: str = None,
    epilog: str | EpilogPart | list[str | EpilogPart] = None,
    **attrs: t.Any,
) -> CliGroup:
    if attrs.get("cls") is None:
        attrs["cls"] = CliGroup
    attrs.setdefault("short_help", short_help)
    attrs.setdefault("epilog", epilog)

    return t.cast(CliGroup, click.group(name, **attrs))


def cli_command(
    name: str,
    short_help: str = None,
    cls: type = CliCommand,
    type: CommandType = CMDTYPE_DEFAULT,
    **attrs: t.Any,
) -> CliCommand:
    attrs.setdefault("short_help", short_help)
    attrs.setdefault("type", type)

    return t.cast(CliCommand, click.command(name, cls, **attrs))


def cli_argument(*param_decls: str, **attrs: t.Any) -> t.Callable[[FC], FC]:
    def decorator(f: FC) -> FC:
        ArgumentClass = attrs.pop("cls", None) or Argument
        _param_memo(f, ArgumentClass(param_decls, **attrs))
        return f

    return decorator


def cli_option(
    *param_decls: str,
    help: str,
    cls=CommandOption,
    **attrs: t.Any,
) -> t.Callable[[FC], FC]:
    attrs.setdefault("help", help)

    def decorator(f: FC) -> FC:
        option_attrs = attrs.copy()
        OptionClass = cls or option_attrs.pop("cls", CommandOption)
        _param_memo(f, OptionClass(param_decls, **option_attrs))
        return f

    return decorator


cli_pass_context = click.pass_context
