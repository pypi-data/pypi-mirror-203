# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2021-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

import click

from ._decorators import cli_pass_context, _catch_and_log_and_exit, cli_group
from ..cli import print_regex, print_weather_icons, print_static, print_commands


@cli_group(__file__)
@cli_pass_context
@_catch_and_log_and_exit
def group(ctx: click.Context, **kwargs):
    """Display preset cheatsheet."""


group.add_commands(
    print_regex.RegexPrinter,
    print_weather_icons.WeatherIconsPrinter,
    print_commands.PrintCommandsCommand,
    *print_static.StaticCommandFactory().make_all(),
)
