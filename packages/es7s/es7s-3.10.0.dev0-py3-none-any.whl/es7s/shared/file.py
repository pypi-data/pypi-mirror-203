# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

from __future__ import annotations

import re
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field


@dataclass
class IFile:
    perm: str
    hlinks: str
    owner: str
    size: str
    timestamp: str
    day: str
    month: str
    time_or_year: str
    name_prefix: str = field(init=False, default=" ")
    name: str
    name_extra: str
    cls_char: str = field(init=False, default=" ")

    is_dir: bool = field(init=False, default=False)
    is_link: bool = field(init=False, default=False)
    is_block: bool = field(init=False, default=False)
    is_char: bool = field(init=False, default=False)
    is_socket: bool = field(init=False, default=False)
    is_pipe: bool = field(init=False, default=False)



class PartMatch:
    def __init__(self, *vals: str):
        self.vals: list[re.Pattern] = [re.compile(v) for v in vals]

    def matches(self, target: IFile) -> bool:
        return any(v.search(target.name) for v in self.vals)


class FullMatch(PartMatch):
    def matches(self, target: IFile) -> bool:
        return any(v.fullmatch(target.name) for v in self.vals)


class IFileIconRenderer(metaclass=ABCMeta):
    @abstractmethod
    def render(self, target: IFile) -> str:
        ...


class FileIconRendererFactory:
    @classmethod
    def make(cls, unicode: bool = False):
        if unicode:
            return FileIconRendererUnicode()
        return FileIconRendererNF()


class FileIconRendererUnicode(IFileIconRenderer):
    def render(self, target: IFile) -> str:
        if target.is_link:
            if target.is_dir:
                return "\uf482"  # 
            return "\uf481"  # 
        if target.is_dir:
            return "\uf115"  # 
        if "." in target.name:
            return "\uf15b"  # 
        return "\uf016"  # 


class FileIconRendererNF(IFileIconRenderer):
    FILE_REGEX_MAP = {
        PartMatch(r"\.(conf|ini)$"): "\ue615",  # 
        FullMatch(".editorconfig", "Makefile"): "\ue615",  # 
        FullMatch(".gitconfig"): "\uf1d3",  # 
        PartMatch(r"\.lock$"): "",  #          PartMatch(r"\.(diff|patch)$"): "\uf440",  # 
        PartMatch(r"\.(js)$"): "",  # 
        PartMatch(r"\.(py)$"): "\ue606",  # 
        PartMatch(r"\.(sh)$"): "\uf489",  # 
        PartMatch(r"\.(php)$"): "󰌟",  # 󰌟 |  
        PartMatch(r"\.(phar)$"): "",
        PartMatch(r"\.(txt)$"): "\uf15c",  # 
        PartMatch(r"\.(1)$"): "\uf02d",  # 
        PartMatch(r"\.(jar)$"): "\ue204",  # 
        PartMatch(r"\.(so)$"): "\ue624",  # 
        PartMatch(r"\.(pdf)$"): "\uf1c1",  # 
        PartMatch(r"\.(psd)$"): "\ue7b8",  # 
        PartMatch(r"\.(svg|png|jpg|gif|webp|xcf)$"):
            "\uf1c5",  #   | 
        PartMatch(r"\.(mp3)$"): "\uf001",  # 
        PartMatch(r"\.(css)$"): "\ue749",  # 
        PartMatch(r"\.(html?)$"): "\uf13b",  # 
        PartMatch(r"\.(zip)$"): "\uf410",  # 
        PartMatch(r"\.(log)$"): "\uf18d",  # 
        PartMatch(r"\.(xlsx?)$"): "\uf1c3",  # 
        PartMatch(r"\.(json)$"): "\ue60b",  # 
        PartMatch(r"\.(md)$"): "\uf48a",  # 
        FullMatch("Dockerfile"): "\uf308",  # 
    }
    DIR_REGEX_MAP = {
        FullMatch("config"): "\ue5fc",  # 
        FullMatch(".git"): "\ue5fb",  # 
        FullMatch(".github"): "\ue5fd",  # 
        FullMatch("Downloads"): "\uf498",  # 
        FullMatch("Pictures"): "󰉏",  # 󰉏
    }

    def render(self, target: IFile) -> str:
        if result_class := self.get_icon_by_class(target):
            return result_class

        if result_ext := self._get_icon_by_ext(target):
            return result_ext

        if target.name.startswith('.'):
            if target.is_dir:
                return "\uf413"  #   |  
            else:
                return "\uf016"  # 

        if target.is_dir:
            return "\uf413"  #    |   
        return "\uf016"  #    | 

    def get_icon_by_class(self, target: IFile) -> str | None:
        if target.is_link:
            if target.is_dir:
                return "\uf482"  # 
            return "\uf481"  # 
        if target.is_block:
            return "\ufc29"  # ﰩ
        if target.is_char:
            return "\ue601"  # 
        if target.is_socket:
            return "\uf6a7"  # 
        if target.is_pipe:
            return "\uf731"  # 
        return None

    def _get_icon_by_ext(self, target: IFile) -> str | None:
        mmap =  self.FILE_REGEX_MAP
        if target.is_dir:
            mmap = self.DIR_REGEX_MAP

        for cond, result in mmap.items():
            if cond.matches(target):
                return result
        return None

