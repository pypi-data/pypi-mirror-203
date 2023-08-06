# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
from __future__ import annotations

import click

from . import (
    exec_get_socket,
    exec_hilight_num,
    exec_list_dir,
    exec_notify,
    exec_sun,
    exec_wrap,
    exec_edit_image,
    exec_switch_wspace,
    exec_external,
)
from ._decorators import cli_pass_context, _catch_and_log_and_exit, cli_group


@cli_group(__file__, short_help="run an embed component")
@cli_pass_context
@_catch_and_log_and_exit
def group(ctx: click.Context, **kwargs):
    """
    Commands that invoke one of es7s subsystems that has been made available
    for standalone manual launching via CLI.
    """


group.add_commands(
    exec_get_socket.GetSocketCommand,
    exec_hilight_num.HighlightNumbersCommand,
    exec_edit_image.EditImageCommand,
    exec_list_dir.ListDirCommand,
    exec_notify.NotifyCommand,
    exec_sun.SunCommand,
    exec_switch_wspace.SwitchWorkspaceCommand,
    exec_wrap.WrapCommand,
    *exec_external.make_external_commands(),
)
