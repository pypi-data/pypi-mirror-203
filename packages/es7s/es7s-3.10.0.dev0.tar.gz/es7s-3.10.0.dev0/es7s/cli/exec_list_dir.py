# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
from __future__ import annotations

from datetime import datetime, timedelta
import getpass
import os
import re
import typing as t
from collections import OrderedDict
from dataclasses import dataclass

import click
import pytermor as pt

from ..shared.file import IFileIconRenderer, FileIconRendererFactory, IFile
from ._decorators import (
    cli_pass_context,
    _catch_and_log_and_exit,
    cli_option,
    cli_argument,
    cli_command,
)
from ..shared import (
    get_stdout,
    get_logger,
    stream_subprocess,
    Styles as StylesShared,
    init_io,
    init_logger,
)
from ..shared.path import LS_PATH


@cli_command(name=__file__, short_help="list directory contents with bells and whistes")
@cli_argument("file", type=str, required=False, nargs=-1)
@cli_option(
    "-g",
    "--groups",
    is_flag=True,
    help="@TODO",
)
@cli_option(
    "-h",
    "--hard-links",
    is_flag=True,
    help="Display amount of hard links to the file",
)
@cli_option(
    "-L",
    "--dereference",
    is_flag=True,
    help="Follow the symlinks and print actual file properties instead of link file properties.",
)
@cli_option(
    "-o",
    "--octal-perms",
    is_flag=True,
    help="Display extra column with permissions in octal form (e.g., 0644, 0755).",
)
@cli_option(
    "-Q",
    "--quote-names",
    is_flag=True,
    help="Enclose filenames in quotes and escape non-printables.",
)
@cli_option(
    "-r",
    "--reverse",
    is_flag=True,
    help="Reverse sorting order.",
)
@cli_option(
    "-R",
    "--recursive",
    is_flag=True,
    help="Descend into subdirectories.",
)
@cli_option(
    "-s",
    "--sort-by-size",
    is_flag=True,
    help="Sort list by file size (directories are unaffected), biggest last.",
)
@cli_option(
    "-t",
    "--sort-by-time",
    is_flag=True,
    help="Sort list by modification time, newest last.",
)
@cli_option(
    "-U",
    "--unicode-icons",
    is_flag=True,
    help="Use shorter icon set (5 items) which should be supported by literally everything down "
    "to a potato (inclusive).",
)
@cli_pass_context
@_catch_and_log_and_exit
class ListDirCommand:
    """
    Wrapper around GNU 'ls' with preset settings for "one-button" usage.
    FILE is a path(s) to directories and files of interest and can be used
    multiple times, default is current/working directory.

    Involves and formats the output of '/usr/bin/ls'. Default format is long,
    entries are sorted by file name, file sizes are in human-readable SI-form.
    No dereferencing is performed.
    """

    # COUNT_CHILDREN_CMD = [
    #     "find",
    #     "%(file)s",
    #     "-maxdepth", "1",
    #     "-type", "d",
    #     "-exec", "sh", "-c", "find {} -maxdepth 1 | wc -l",
    #     ";",
    #     "-print",
    # ]

    SPLIT_REGEX = re.compile(r"(\S+)")
    ATTR_AMOUNT = 10
    OUT_COL_SEPARATOR = " "

    def __init__(
        self,
        ctx: click.Context,
        *,
        file: t.Tuple[str],
        dereference: bool,
        groups: bool,
        hard_links: bool,
        octal_perms: bool,
        quote_names: bool,
        recursive: bool,
        reverse: bool,
        sort_by_size: bool,
        sort_by_time: bool,
        unicode_icons: bool,
        **kwargs,
    ):
        ls_reverse_arg = reverse
        if sort_by_size or sort_by_time:
            ls_reverse_arg = not reverse
        color = "always" if get_stdout().sgr_allowed else "never"
        quoting_style = "shell-escape-always" if quote_names else "literal"

        ls_args = [
            LS_PATH,
            "-l",
            "--no-group",
            "--classify",
            "--almost-all",
            "--si",
            "--group-directories-first",
            "--time-style=+%s %e %b  %Y\n%s %e %b %R",
            "--color=" + color,
            "--quoting-style=" + quoting_style,
            "-t" if sort_by_time else "",
            "-S" if sort_by_size else "",
            "--reverse" if ls_reverse_arg else "",
            "--recursive" if recursive else "",
            "--dereference" if dereference else "",
        ]
        self._custom_columns = dict(
            octperms=octal_perms,
            hlinks=hard_links,
            groups=groups,
        )
        self._icon_renderer = FileIconRendererFactory.make(unicode_icons)
        self._run(file, *filter(None, ls_args))

    def _run(self, file: t.Tuple[str], *ls_args: str):
        ls_args += ("--", *file)

        for out, err in stream_subprocess(*ls_args):
            if out and (line := self._process_ls_output(out.rstrip())):
                get_stdout().echo(line)
            if err:
                get_logger().error(err.rstrip())

    def _process_ls_output(self, line: str) -> str:
        if line.startswith("total"):
            return get_stdout().echo_rendered(_highligher.colorize(line))
        try:
            return self._process_regular_line(line)
        except ValueError:
            return line

    def _process_regular_line(self, line: str) -> str:
        splitted = list(self._split_ls_line(line))
        if len(splitted) != self.ATTR_AMOUNT:
            return line

        file = File(*splitted)
        columns = file.render(self._custom_columns, self._icon_renderer)
        filtered_columns = self._assemble_line(columns)
        return self.OUT_COL_SEPARATOR.join(filtered_columns)

    def _assemble_line(self, render_parts: OrderedDict) -> t.Iterable[str]:
        for k, v in render_parts.items():
            if not self._custom_columns.get(k, True):
                continue
            yield v

    def _split_ls_line(self, s: str) -> tuple[str, ...]:
        splitted = self.SPLIT_REGEX.split(s, self.ATTR_AMOUNT - 1)
        pairs = [iter(splitted)] * 2
        for value in zip(*pairs, strict=False):
            yield "".join(value)  # value ex.: (' ', '461')
        yield splitted[-1]


class Styles(StylesShared):
    @staticmethod
    def _make_rwx(r: pt.FT, w: pt.FT, x: pt.FT, base: pt.Style = pt.NOOP_STYLE) -> t.Dict:
        return {k: pt.Style(base, fg=v) for k, v in dict(r=r, w=w, x=x).items()}

    INACTIVE = StylesShared.TEXT_LABEL
    INACTIVE_ATTR = StylesShared.TEXT_DISABLED
    OCTAL_PERMS = pt.Style(fg=pt.cv.MAGENTA)
    OCTAL_PERMS_1ST_ZERO = pt.Style(OCTAL_PERMS, dim=True)
    OCTAL_PERMS_1ST_NONZERO = pt.Style(OCTAL_PERMS)
    HARD_LINKS_DIR = INACTIVE
    HARD_LINKS_FILE = pt.Style(fg=pt.cv.RED, bold=True)
    HARD_LINKS_FILE_GT1 = pt.Style(fg=pt.cv.HI_YELLOW, bg=pt.cv.RED, bold=True)
    SPECIAL_ATTR_L = pt.Style(fg=pt.Color256.get_by_code(68))
    SPECIAL_ATTR_U = pt.Style(fg=pt.Color256.get_by_code(74), bold=True)
    EXTENDED_ATTR = pt.Style(fg="true-white")
    OWNER_COLOR_ROOT = pt.cv.HI_RED
    OWNER_COLOR_CURUSER = pt.NOOP_COLOR
    OWNER_COLOR_OTHER = pt.cv.HI_YELLOW  # not current and not root

    RWX_MAP = {
        "user": _make_rwx("hi-red kalm", "yellow kalm", "hi-yellow kalm", pt.Style(bold=True)),
        "group": _make_rwx(0x794544, 0x79513D, 0x8D7951),
        "others": _make_rwx(0x5F4A49, 0x635149, 0x625E56),
    }  # r         w         x
    RWX_MAP_256 = {
        "user": _make_rwx("hi-red", "yellow", "hi-yellow", pt.Style(bold=True)),
        "group": _make_rwx("hi-red", "yellow", "hi-yellow", pt.Style(dim=True)),
        "others": _make_rwx(pt.cv.GRAY_30, pt.cv.GRAY_35, pt.cv.GRAY_42),
    }


_highligher = pt.Highlighter(dim_units=False)


@dataclass
class File(IFile):
    NO_SIZE_PERM_REGEX = re.compile("^[d]")
    UNKNOWN_SIZE_PERM_REGEX = re.compile("^[l]")
    INACTIVE_ATTR_REGEX = re.compile("([-?]+)")
    FILE_CLASS_REGEX = re.compile(r"([*/=>@|]?)$")  # there will be \e[m SGR or \e]K
    SGR_SEQ_REGEX = re.compile(r"(\x1b)(\[)([0-9;]*)(m)")

    def __post_init__(self):
        self._inactive_attr_replace = get_stdout().render(r"\1", Styles.INACTIVE)

        self.name_prefix = ""
        self.name += self.name_extra
        self.name_extra = ""

        if cls_match := self.FILE_CLASS_REGEX.search(self.name):
            self.cls_char = cls_match.group(1) or " "
            self.name = self.name.removesuffix(self.cls_char)

        match self.cls_char:
            case "/":
                self.is_dir = True

        match self.perm[0]:
            case "l":
                self.is_link = True
            case "c":
                self.is_char = True
            case "b":
                self.is_block = True
            case "s":
                self.is_socket = True
            case "p":
                self.is_pipe = True

    def render(self, custom_columns: dict, icon_renderer: IFileIconRenderer) -> OrderedDict:
        filefmt: str = ""

        def found(sgrm: re.Match):
            # to correctly process lines like: 4-Oct␣14:00␣⢸θ⡇⢸ǝF66⡇.aptitude⢸θ⡇/↵
            # adding resetter 0m to fmt will make it useless, so omit it
            nonlocal filefmt
            if sgrm.group(3) in ["", "0"] and len(filefmt) > 0:
                return ""
            filefmt += sgrm.group()
            return ""

        if get_stdout().renderer.is_format_allowed:
            # extract existing SGRs (from ls) and reapply them to bigger set of fields
            self.name = pt.utilstr.SGR_SEQ_REGEX.sub(found, self.name)
            if name_prefix := re.match(r"^\s+", self.name):
                self.name_prefix = name_prefix.group()
                self.name = self.name[len(self.name_prefix) :]

        sgr_reset = pt.SeqIndex.RESET.assemble()
        perm_render, perm_raw = self._render_perm()
        if not custom_columns.get("octperms", False):
            perm_render = " " + perm_render
        return OrderedDict(
            octperms=self._render_oct_perm(perm_raw),
            perms=perm_render,
            hlinks=self._render_hlinks(),
            owner=self._render_owner(),
            size=self._render_size(),
            date=self._render_date(),
            fclass=(filefmt + self._render_class() + sgr_reset),
            fname=(filefmt + icon_renderer.render(self) + self._render_name() + sgr_reset),
        )

    def _render_oct_perm(self, perm_raw: str) -> str:
        def get_st(val: int, pos: int) -> pt.Style:
            if pos > 0:
                return Styles.OCTAL_PERMS
            if val > 0:
                return Styles.OCTAL_PERMS_1ST_NONZERO
            return Styles.OCTAL_PERMS_1ST_ZERO

        perms = pt.Text()
        for n in range(3):
            ppart = perm_raw[n*3:(n+1)*3]
            ppart_int = 0
            for idx, val in enumerate([4, 2, 1]):
                if ppart[idx].islower():
                    ppart_int += val
            perms.append(pt.Fragment(str(ppart_int), get_st(ppart_int, n+1)))

        specials = perm_raw[2] + perm_raw[5] + perm_raw[8]
        spart_int = 0
        for idx, val in enumerate([4, 2, 1]):
            if specials[idx].lower() in ("s", "t"):
                spart_int += val
        perms.prepend(pt.Fragment(str(spart_int or " "), get_st(spart_int, 0)))

        return get_stdout().render(perms)

    def _render_perm(self) -> tuple[str, str]:
        raw = self.perm[1:]
        if not raw.endswith("+"):
            raw += " "

        result = pt.Text()
        for idx, c in enumerate(raw):
            result += pt.Fragment(*self._render_perm_chars(idx, c))
        return get_stdout().render(result), result.render(pt.renderer.NoOpRenderer)

    def _render_perm_chars(self, idx: int, c: str) -> tuple[str, pt.FT]:
        match c:
            case "+":
                return c, Styles.EXTENDED_ATTR
            case "-":
                return c, Styles.INACTIVE_ATTR
            case "s" | "t":
                return c, Styles.SPECIAL_ATTR_L
            case "S" | "T":
                return c, Styles.SPECIAL_ATTR_U
            case "r" | "w" | "x":
                if idx < 3:
                    rwx_set = Styles.RWX_MAP.get("user")
                elif idx < 6:
                    rwx_set = Styles.RWX_MAP.get("group")
                else:
                    rwx_set = Styles.RWX_MAP.get("others")
                return c, rwx_set.get(c)
            case " ":  # padding
                return c, pt.NOOP_STYLE
            case _:  # unknown
                return c, Styles.CRITICAL_ACCENT

    def _render_owner(self) -> str:
        def _cur_user() -> str:
            try:
                return os.getlogin()
            except OSError:
                return getpass.getuser()

        owner = self.owner.removeprefix(" ")
        if owner == "root":
            st = Styles.OWNER_COLOR_ROOT
        elif owner == _cur_user():
            st = Styles.OWNER_COLOR_CURUSER
        else:
            st = Styles.OWNER_COLOR_OTHER

        return get_stdout().render(owner, st)

    def _render_hlinks(self) -> str:
        hlinks_style = Styles.INACTIVE
        if not self.is_dir:
            hlinks_style = Styles.HARD_LINKS_FILE
            if int(self.hlinks) > 1:
                hlinks_style = Styles.HARD_LINKS_FILE_GT1
        return get_stdout().render(f"{self.hlinks}", hlinks_style)

    def _render_size(self) -> str:
        def get_inactive_label() -> str|None:
            if self.UNKNOWN_SIZE_PERM_REGEX.match(self.perm):
                return "?"
            if self.NO_SIZE_PERM_REGEX.match(self.perm):
                return "-"

        if inactive_label := get_inactive_label():
            return get_stdout().render(inactive_label.rjust(len(self.size)), Styles.INACTIVE)
        return get_stdout().render(_highligher.colorize(self.size))

    def _render_date(self) -> str:
        datefmt = pt.NOOP_SEQ
        if get_stdout().renderer.is_format_allowed:
            diff = datetime.now() - datetime.fromtimestamp(int(self.timestamp))
            datefmt = self._get_date_format(diff)
        return (
            f"{datefmt}{self.day}{self.month}{self.time_or_year}{pt.ansi.get_closing_seq(datefmt)}"
        )

    def _render_class(self) -> str:
        if self.is_block:
            return "+"
        if self.is_char:
            return "-"
        if self.is_link:
            return "~" if self.is_dir else "@"
        if self.is_socket:
            return "="
        if self.is_pipe:
            return "|"
        return self.cls_char

    def _render_name(self) -> str:
        if self.is_link:
            self.name = self.name.replace("->", "⇒")
        return self.name_prefix + self.name

    def _auto_apply_inactive_style(self, string: str) -> str:
        return re.sub(self.INACTIVE_ATTR_REGEX, self._inactive_attr_replace, string)

    @staticmethod
    def _get_date_format(diff: timedelta) -> pt.SequenceSGR:
        if diff < timedelta(hours=1):
            code = 231  # true white
        elif diff < timedelta(days=7):
            code = 254  # 89% gray
        elif diff < timedelta(days=30):
            code = 253 - (3 * diff.days // (30 - 7))  # 253-250 (85-74%)
        elif diff < timedelta(days=365 * 12):
            code = 249 - (diff.days // 365)  # 249-237 (70-23%)
        else:
            code = 237  # 23% gray
        return pt.make_color_256(code)


if __name__ == "__main__":
    init_io()
    init_logger()
    try:
        ListDirCommand().run()
    except Exception as e:
        get_logger().exception(e)
        exit(1)
