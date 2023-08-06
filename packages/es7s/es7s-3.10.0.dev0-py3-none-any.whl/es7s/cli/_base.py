# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
from __future__ import annotations

import inspect
import re
import typing as t
from dataclasses import dataclass
from os.path import basename, dirname, splitext, isfile, join
from typing import cast, overload

import click
import pytermor as pt

from ._base_opts_params import OptionScope, ScopedOption, EpilogPart, EPILOG_COMMAND_HELP, \
    EPILOG_COMMON_OPTIONS, EPILOG_ARGS_NOTE, CommandType, CMDTYPE_DEFAULT, CMDTYPE_GROUP
from .. import APP_NAME
from ..shared import (
    get_logger,
    get_stdout,
    format_attrs,
    Styles,
)


@dataclass(frozen=True)
class Examples:
    title: str
    content: t.Sequence[str]

    def __bool__(self) -> bool:
        return len(self.content) > 0


# fmt: off
class HelpStyles(Styles):
    TEXT_HEADING = pt.Style(fg=pt.cv.YELLOW, bold=True)       # SYNOPSIS      |   | explicit manual usage only      # noqa
    TEXT_COMMAND_NAME = pt.Style(fg=pt.cv.BLUE)               # es7s exec     |   | auto-detection                  # noqa
    TEXT_OPTION_DEFAULT = pt.Style(fg=pt.cv.HI_YELLOW)        # [default: 1]  |[ ]| requires wrapping in [ ]        # noqa
    TEXT_LITERAL = pt.Style(bold=True)                        # 'ls | cat'    | ' | non-es7s commands (punctuation) # noqa
    TEXT_LITERAL_WORDS = pt.Style(underlined=True)            # 'ls | cat'    | ' | non-es7s commands (words)       # noqa
    TEXT_EXAMPLE = pt.Style(fg=pt.cv.CYAN, bg='full-black')   # ` 4 11`       | ` | output example                  # noqa
    TEXT_ENV_VAR = pt.Style(fg=pt.cv.GREEN, bold=True)        # {ES7S_LE_VAR} |{ }| environment variable name       # noqa
    TEXT_ABOMINATION = pt.Style(bg=pt.cv.BLUE).autopick_fg()  # ::NOTE::      |:: | needs to be wrapped in ::       # noqa
    TEXT_INLINE_CONFIG_VAR = pt.Style(fg=pt.cv.MAGENTA)       # <section.opt> |< >| config variable name            # noqa
    TEXT_ALTER_MODE = pt.Style(italic=True)                   # ^ALT MODE^    |^ ^| alt monitor mode                # noqa
    TEXT_COMMENT = pt.Style(fg=pt.cv.GRAY)                    # // COMMENT    |// | till end of the line            # noqa
    TEXT_ACCENT = pt.Style(bold=True)                         # *important*   | * | needs to be wrapped in *        # noqa
                                                                #  '--option' | ' | auto-detection if wrapped in '  # noqa
                                                                #  "--option" | " | " -> space instead of removing  # noqa
# fmt: on


class HelpFormatter(click.HelpFormatter):
    # fmt: off
    OPT_DEFAULT_REGEX = re.compile(r"(default:\s*)(.+?)([];])|(\[[\w\s]+)(default)(])")

    OPT_REF_REGEX = re.compile(r"'(\n\s*)?(--?[\w-]+)'")
    OPT_REF_FIX_REGEX = re.compile(r'"(\n\s*)?(--?[\w-]+)"')  # < @TODO join with regular
    ACCENT_REGEX = re.compile(r"(^|)?\*([\w!-]+?)\*")
    LITERAL_REGEX = re.compile(r"'(\n\s*)?([\w/ \n|-]+?)'")
    EXAMPLE_REGEX = re.compile(r"`(\n\s*)?(.+?)`")
    INLINE_CONFIG_VAR_REGEX = re.compile(r"<(\n\s*)?([\w\s.-]+?)>")
    ENV_VAR_REGEX = re.compile(r"\{(\n\s*)?([\w.-]+?)}")  # @FIXME join with other wrappers?
    INLINE_ENV_VAR_REGEX = re.compile(r"@([()\w._-]+?)@")  # @FIXME join with other wrappers?
    ABOMINATION_REGEX = re.compile(r"::([\w.-]+?:*)::")
    ALTER_MODE_REGEX = re.compile(r"\^([\w .!-]+?)\^")
    COMMENT_REGEX = re.compile(r"(\s//\s?)(.+)($)")
    COMMENT_BLOCK_REGEX = re.compile(r"/\*()(.+)()\*/", flags=re.DOTALL)
    # fmt: on

    def __init__(
        self,
        indent_increment: int = 2,
        width: t.Optional[int] = None,
        max_width: t.Optional[int] = None,
    ):
        width = pt.get_preferable_wrap_width(False)
        super().__init__(indent_increment, width, max_width)

        self.help_filters: t.List[pt.StringReplacer] = [
            pt.StringReplacer(self.OPT_DEFAULT_REGEX, self.format_option_default),
            pt.StringReplacer(self.OPT_REF_REGEX, self.format_accent),
            pt.StringReplacer(self.OPT_REF_FIX_REGEX, self.format_accent_fixed),
            pt.StringReplacer(self.ACCENT_REGEX, self.format_accent),
            pt.StringReplacer(self.LITERAL_REGEX, self.format_literal),
            pt.StringReplacer(self.EXAMPLE_REGEX, self.format_example),
            pt.StringReplacer(self.INLINE_CONFIG_VAR_REGEX, self.format_inline_config_var),
            pt.StringReplacer(self.ENV_VAR_REGEX, self.format_env_var),
            pt.StringReplacer(self.INLINE_ENV_VAR_REGEX, self.format_inline_env_var),
            pt.StringReplacer(self.ABOMINATION_REGEX, self.format_abomination),
            pt.StringReplacer(self.ALTER_MODE_REGEX, self.format_alter_mode),
            pt.StringReplacer(self.COMMENT_REGEX, self.format_comment),
            pt.StringReplacer(self.COMMENT_BLOCK_REGEX, self.format_comment),
        ]

        self.command_names = [APP_NAME]
        if (ctx := click.get_current_context(True)) is None:
            return
        self.command_names = self._find_all_command_names(ctx.find_root().command)

    def _find_all_command_names(self, command: click.Command) -> set[str]:
        names = set()
        names.add(command.name)
        if hasattr(command, "commands") and isinstance(command.commands, dict):
            for nested_command in command.commands.values():
                names = names.union(self._find_all_command_names(nested_command))
        return names

    def format_option_default(self, m: re.Match) -> str:
        return (
            (m.group(1) or m.group(4))
            + get_stdout().render(m.group(2) or m.group(5), HelpStyles.TEXT_OPTION_DEFAULT)
            + (m.group(3) or m.group(6))
        )

    def format_command_name(self, arg: re.Match | str) -> str:
        if isinstance(arg, re.Match):
            arg = arg.group(1)
        return get_stdout().render(arg, HelpStyles.TEXT_COMMAND_NAME)

    def format_command_type(self, ct: CommandType) -> str:
        if not ct.char:
            return " "
        return get_stdout().render(ct.char, ct.fmt)

    def format_command_type_desc(self, ct: CommandType) -> str:
        return "[" + self.format_command_type(ct) + "] " + ct.name

    @overload
    def format_command_name_and_type(self, ct: CommandType, cmd_name: str) -> str:
        ...

    @overload
    def format_command_name_and_type(self, cmd: CliBaseCommand) -> str:
        ...

    def format_command_name_and_type(self, *args) -> str:
        if len(args) == 1:
            cmd = args[0]
            return self.format_command_name_and_type(cmd.get_command_type(), cmd.name)
        ct, cmd_name = args
        return self.format_command_type(ct) + " " + self.format_command_name(cmd_name)

    def format_accent(self, m: re.Match) -> str:
        return get_stdout().render((m.group(1) or "") + m.group(2), HelpStyles.TEXT_ACCENT)

    def format_accent_fixed(self, m: re.Match) -> str:
        return get_stdout().render(
            " " + (m.group(1) or "") + m.group(2) + " ", HelpStyles.TEXT_ACCENT
        )

    def format_example(self, m: re.Match) -> str:
        return get_stdout().render((m.group(1) or "") + m.group(2), HelpStyles.TEXT_EXAMPLE)

    def format_inline_config_var(self, m: re.Match) -> str:
        result = m.group(1) or ""
        return result + ".".join(
            get_stdout().render(name, HelpStyles.TEXT_INLINE_CONFIG_VAR)
            for name in re.split(r"\.\s*", m.group(2))
        )

    def format_env_var(self, m: re.Match):
        return get_stdout().render(
            (m.group(1) or "") + " " + m.group(2) + " ", HelpStyles.TEXT_ENV_VAR
        )

    def format_inline_env_var(self, m: re.Match):
        return get_stdout().render(m.group(1), HelpStyles.TEXT_ENV_VAR)

    def format_abomination(self, m: re.Match):
        return " " + get_stdout().render(" " + m.group(1) + " ", HelpStyles.TEXT_ABOMINATION) + " "

    def format_alter_mode(self, m: re.Match):
        return get_stdout().render(m.group(1), HelpStyles.TEXT_ALTER_MODE) + "  "

    def format_comment(self, m: re.Match):
        return (
            "." * len(m.group(1))
            + get_stdout().render(m.group(2), HelpStyles.TEXT_COMMENT)
            + ":" * len(m.group(3))
        )

    def format_heading(self, s: str) -> str:
        return get_stdout().render(s, HelpStyles.TEXT_HEADING)

    def format_literal(self, sm: re.Match) -> str:
        text_literal_is_present = False
        word_count = 0

        def replace_literal(wm: re.Match) -> str:
            nonlocal text_literal_is_present, word_count
            word_count += 1
            word = wm.group()
            if len(word) < 2:
                text_literal_is_present = True
                style = HelpStyles.TEXT_LITERAL
            elif word in self.command_names or word.startswith(APP_NAME):
                style = HelpStyles.TEXT_COMMAND_NAME
            elif word.startswith("-"):
                style = HelpStyles.TEXT_ACCENT
            else:
                text_literal_is_present = True
                style = HelpStyles.TEXT_LITERAL_WORDS
            return get_stdout().render(word, style)

        replaced = re.sub(r"(\S+)", replace_literal, (sm.group(1) or "") + sm.group(2))
        if text_literal_is_present and word_count > 1:
            replaced = f"'{replaced}'"
        return replaced

    def write_heading(self, heading: str, newline: bool = False, colon: bool = True):
        heading = get_stdout().render(heading + (colon and ":" or ""), HelpStyles.TEXT_HEADING)
        self.write(f"{'':>{self.current_indent}}{heading}")
        self.write_paragraph()
        if newline:
            self.write_paragraph()

    def write_squashed_text(self, string: str):
        indent = " " * self.current_indent
        wrapped_text = click.wrap_text(
            string,
            self.width,
            initial_indent=indent,
            subsequent_indent=indent,
            preserve_paragraphs=True,
        )
        self.write(wrapped_text.replace("\n\n", "\n"))
        self.write("\n")

    def write(self, string: str) -> None:
        stripped = string.strip()
        if stripped in self.command_names:
            string = get_stdout().render(string, HelpStyles.TEXT_COMMAND_NAME)
        if stripped.startswith(APP_NAME):
            string = re.sub("([a-z0-9_-]+)", lambda m: self.format_command_name(m), string, 3)
        else:
            string = pt.utilstr.apply_filters(string, *self.help_filters)
        self.buffer.append(string)


class Context(click.Context):
    formatter_class = HelpFormatter

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.failed = False
        self.color = get_stdout().color

    def fail(self, message: str):
        self.failed = True
        super().fail(message)



class CliBaseCommand(click.Command):
    context_class = Context

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("type", CMDTYPE_DEFAULT)
        self._command_type: CommandType = kwargs.pop("type")

        super().__init__(*args, **kwargs)

    def get_command_type(self) -> CommandType:
        return self._command_type

    def parse_args(self, ctx: Context, args: t.List[str]) -> t.List[str]:
        get_logger().debug(f"Pre-click args:  {format_attrs(args)}")
        parsed_args = super().parse_args(ctx, args)
        return parsed_args

    def invoke(self, ctx: Context) -> t.Any:
        get_logger().debug(f"Post-click args: {format_attrs(ctx.params)}")
        try:
            return super().invoke(ctx)
        except click.ClickException as e:
            ctx.failed = True
            self.show_error(ctx, e)

    def show_error(self, ctx: Context, e: click.ClickException):
        logger = get_logger()
        logger.error(e.format_message())
        if logger.quiet:
            return

        hint = ""
        if ctx.command.get_help_option(ctx):
            hint = f"\nTry '{ctx.command_path} {ctx.help_option_names[0]}' for help."
        get_stdout().echo(f"{ctx.get_usage()}\n{hint}")

    def _make_command_name(self, orig_name: str) -> str:
        dir_name = dirname(orig_name)
        filename_parts = splitext(basename(orig_name))[0].lstrip("_").split("_")
        if filename_parts[0] == "group":
            filename_parts.pop(0)
        if len(filename_parts) == 1:
            return filename_parts[0]
        while filename_parts:
            if isfile(join(dir_name, f"group_{filename_parts[0]}.py")):
                filename_parts.pop(0)
                continue
            return "-".join(filename_parts)

    def _make_short_help(self, **kwargs) -> str:
        help_str = kwargs.get("help")
        if not help_str:
            if logger := get_logger(require=False):
                logger.warning(f"Missing help for '{kwargs.get('name')}' command")
            help_str = "..."

        short_help = kwargs.get("short_help")
        short_help_auto = help_str.lower().removesuffix(".")
        if isinstance(short_help, t.Callable):
            return short_help(short_help_auto)
        elif short_help:
            return short_help
        return short_help_auto

    def format_epilog(self, ctx: Context, formatter: HelpFormatter) -> None:
        epilog_parts = []

        if self.epilog:
            if not isinstance(self.epilog, list):
                self.epilog = [self.epilog]
            epilog_parts.extend(self.epilog)

        if any(self._is_option_with_argument(opt) for opt in ctx.command.params):
            epilog_parts.append(EPILOG_ARGS_NOTE)

        if self._include_common_options_epilog():
            epilog_parts.append(EPILOG_COMMON_OPTIONS)

        if isinstance(self, click.Group):
            epilog_parts.append(
                EpilogPart(
                    EPILOG_COMMAND_HELP.text % (ctx.command_path, ctx.command_path, [*self.commands.values()][0].name),
                    group=EPILOG_COMMAND_HELP.group,
                    )
            )

        self._format_epilog_parts(formatter, epilog_parts)

    def _include_common_options_epilog(self) -> bool:
        return True

    def _is_option_with_argument(self, option: click.Parameter) -> bool:
        if isinstance(option, ScopedOption):
            return option.has_argument()
        return False

    def _format_epilog_parts(self, formatter: HelpFormatter, parts: list[EpilogPart]):
        squashed_parts = []
        for idx, part in enumerate(parts):
            if (
                len(squashed_parts)
                and not part.title
                and part.group
                and part.group == squashed_parts[-1].group
            ):
                squashed_parts[-1].text += "\n\n" + part.text
                continue
            squashed_parts.append(part)

        for part in squashed_parts:
            self._format_epilog_part(formatter, part)

    def _format_epilog_part(self, formatter: HelpFormatter, part: EpilogPart):
        formatter.write_paragraph()
        if part.title:
            formatter.write_heading(part.title.capitalize(), newline=True, colon=False)

        with formatter.indentation():
            formatter.write_squashed_text(inspect.cleandoc(part.text))


class CliCommand(CliBaseCommand):
    option_scopes: list[OptionScope] = [
        OptionScope.COMMAND,
        OptionScope.GROUP,
    ]

    def __init__(self, **kwargs):
        kwargs.update(
            {
                "name": self._make_command_name(kwargs.get("name")),
                "params": self._build_options(kwargs.get("params", [])),
                "short_help": self._make_short_help(**kwargs),
            }
        )
        self.command_examples = Examples("Command examples", kwargs.pop("command_examples", []))
        self.output_examples = Examples("Output examples", kwargs.pop("output_examples", []))

        super().__init__(**kwargs)

    def _build_options(self, subclass_options: list[ScopedOption]) -> list[ScopedOption]:
        return [
            *subclass_options,
            *self._get_group_options(),
        ]

    def _get_group_options(self) -> list[ScopedOption]:
        return []

    def format_usage(self, ctx: Context, formatter: HelpFormatter) -> None:
        pieces = self.collect_usage_pieces(ctx)
        with formatter.section("Usage"):
            formatter.write_usage(ctx.command_path, " ".join(pieces), prefix="")

    def format_help_text(self, ctx: Context, formatter: HelpFormatter) -> None:
        super().format_help_text(ctx, formatter)
        self.format_examples(ctx, formatter, self.output_examples)
        self.format_command_type(ctx, formatter)

    def format_command_type(self, ctx: Context, formatter: HelpFormatter):
        if (ct := self.get_command_type()) in (CMDTYPE_DEFAULT, CMDTYPE_GROUP):
            return

        formatter.write_paragraph()
        with formatter.indentation():
            ct_icon = get_stdout().render(
                f'{ct.char or " ":^3s}',
                pt.Style(pt.make_style(ct.fmt), bold=True, inversed=True),
            )
            formatter.write_dl([(ct_icon, ct.description)])

    def format_options(self, ctx: Context, formatter: HelpFormatter):
        opt_scope_to_opt_help_map: dict[str, list[tuple[str, str]] | None] = {
            k: [] for k in OptionScope
        }
        for param in self.get_params(ctx):
            rv = param.get_help_record(ctx)
            if rv is not None and hasattr(param, "scope"):
                opt_scope_to_opt_help_map[param.scope].append(rv)

        for opt_scope in self.option_scopes:
            opt_helps = opt_scope_to_opt_help_map[opt_scope]
            if not opt_helps:
                continue
            if opt_scope.value:
                with formatter.section(opt_scope.value):
                    formatter.write_dl(opt_helps)
            else:
                formatter.write_paragraph()
                with formatter.indentation():
                    formatter.write_dl(opt_helps)

    def format_epilog(self, ctx: Context, formatter: HelpFormatter) -> None:
        super().format_epilog(ctx, formatter)
        self.format_examples(ctx, formatter, self.command_examples)

    def format_examples(self, ctx: Context, formatter: HelpFormatter, examples: Examples) -> None:
        if not examples:
            return
        with formatter.section(examples.title.capitalize()):
            for example in examples.content:
                if "%s" in example:
                    example %= ctx.command_path
                formatter.write_text(example)


class CliGroup(click.Group, CliBaseCommand):
    def __init__(self, **kwargs):
        kwargs["name"] = self._make_command_name(kwargs.get("name"))
        kwargs["short_help"] = self._make_short_help(**kwargs)
        kwargs.setdefault("type", CMDTYPE_GROUP)

        super().__init__(**kwargs)

    def format_usage(self, ctx: Context, formatter: HelpFormatter) -> None:
        pieces = self.collect_usage_pieces(ctx)
        with formatter.section("Usage"):
            formatter.write_usage(ctx.command_path, " ".join(pieces), prefix="")

    def format_commands(self, ctx: Context, formatter: HelpFormatter) -> None:
        # modified version of parent implementation; could not inject otherwise
        commands = []
        for subcommand in self.list_commands(ctx):
            cmd = self.get_command(ctx, subcommand)
            # What is this, the tool lied about a command.  Ignore it
            if cmd is None:
                continue
            if cmd.hidden:
                continue
            commands.append((subcommand, cmd))

        if len(commands):
            # +2 for command type
            limit = formatter.width - 6 - max(2 + len(cmd[0]) for cmd in commands)

            rows = []
            for subcommand, cmd in commands:
                help = cmd.get_short_help_str(limit)
                cmd_name = formatter.format_command_name_and_type(cmd)
                rows.append((cmd_name, help))

            if rows:
                with formatter.section("Commands"):
                    formatter.write_dl(rows, col_spacing=4)

    def format_options(self, ctx: Context, formatter: HelpFormatter) -> None:
        # no options for groups
        self.format_commands(ctx, formatter)

        cts = [ct for ct in {*self.get_command_types()} if ct.char]

        formatter.write_paragraph()
        with formatter.indentation():
            formatter.write_text("   ".join(formatter.format_command_type_desc(ct) for ct in cts))

    def add_commands(self, *commands: click.Command):
        for cmd in commands:
            self.add_command(cmd)

    def get_commands(self) -> dict[str, CliBaseCommand]:
        return cast(dict[str, CliBaseCommand], self.commands)

    def get_command(self, ctx, cmd_name) -> CliBaseCommand | None:
        rv = super().get_command(ctx, cmd_name)
        if rv is not None:
            return cast(CliBaseCommand, rv)
        matches = [x for x in self.list_commands(ctx) if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return super().get_command(ctx, matches[0])
        ctx.fail(f"Too many matches: {', '.join(sorted(matches))}")

    def resolve_command(self, ctx, args):
        # always return the full command name
        _, cmd, args = super().resolve_command(ctx, args)
        return cmd.name, cmd, args

    def get_command_types(self, recursive: bool = False) -> t.Iterable[CommandType]:
        for cmd in self.get_commands().values():
            if recursive and isinstance(cmd, CliGroup):
                yield from cmd.get_command_types(True)
            yield cmd.get_command_type()

