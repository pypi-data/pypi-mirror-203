# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import typing as t
from typing import cast

import click
import pytermor as pt

from ._base import (
    CliCommand,
    CliGroup,
    HelpFormatter,
    CliBaseCommand,
    HelpStyles,
)
from ._base_opts_params import CMDTYPE_DYNAMIC
from ._decorators import cli_pass_context, _catch_and_log_and_exit, cli_command
from ..shared import get_stdout


@cli_command(
    name=__file__,
    cls=CliCommand,
    type=CMDTYPE_DYNAMIC,
    short_help="list all es7s commands",
)
@cli_pass_context
@_catch_and_log_and_exit
class PrintCommandsCommand:
    """
    Print es7s commands with descriptions as grouped (default) or plain list.
    """

    def __init__(self, ctx: click.Context, **kwargs):
        self._formatter = HelpFormatter()
        self._run(ctx)

    def _run(self, ctx: click.Context):
        from ._entrypoint import root_commands

        lines = [line for line in self._iterate(root_commands, []) if line]
        self._formatter.write_dl(lines)

        self._formatter.write_paragraph()
        root_cmd = cast(CliGroup, ctx.find_root().command)
        with self._formatter.indentation():
            for ct in sorted({*root_cmd.get_command_types(recursive=True)}, key=lambda t: t.sorter):
                if not ct.char:
                    continue
                self._formatter.write_text(self._formatter.format_command_type_desc(ct))

        get_stdout().echo(self._formatter.getvalue())

    def _format_command(self, cmd: CliBaseCommand, stack: list[str]) -> tuple[str, str]|None:
        cname = ' '.join(stack + [cmd.name])
        offset = len(stack) * 3 * " "
        ctype_str = self._formatter.format_command_type(cmd.get_command_type())
        cname_str = get_stdout().render(cname, pt.Style(HelpStyles.TEXT_COMMAND_NAME, bold=len(stack)==0))
        return offset + ctype_str + " " + cname_str,  cmd.get_short_help_str()

    def _format_group(self, cmd: CliBaseCommand, stack: list[str]) -> tuple[str, str]|None:
        cname = ' '.join(stack + [cmd.name])
        return self._formatter.format_heading("  " +cname), ""

    def _iterate(self, cmds: t.Iterable[CliBaseCommand], stack: list[str] = None):
        for cmd in sorted(cmds, key=lambda c: c.name):
            if not isinstance(cmd, CliGroup):
                yield self._format_command(cmd, stack)
            else:
                yield self._format_group(cmd, stack)
                yield from self._iterate(cmd.get_commands().values(), stack + [cmd.name])
