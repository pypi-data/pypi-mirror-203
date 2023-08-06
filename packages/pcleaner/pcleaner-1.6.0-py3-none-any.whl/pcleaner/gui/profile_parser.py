from pathlib import Path
from typing import get_type_hints
from dataclasses import dataclass, field
from enum import Enum, auto
import re

import configupdater as cu
from logzero import logger

from pcleaner import config as cfg


class EntryTypes(Enum):
    """
    The different types of entries in a profile.
    """

    Bool = auto()
    Int = auto()
    Float = auto()
    Str = auto()
    StrNone = auto()
    Color = auto()


@dataclass(frozen=True)
class ProfileComment:
    comment: str


@dataclass(frozen=True)
class ProfileEntry:
    key: str
    entry_type: EntryTypes


@dataclass(frozen=True)
class ProfileSection:
    name: str
    items: list[ProfileComment | ProfileEntry] = field(default_factory=list)


def parse_profile_structure(profile: cfg.Profile) -> list[ProfileSection]:
    """
    Parse the given profile and return an intermediate representation,
    Such that it can be used by the GUI.

    This representation doesn't contain any values, only the structure.

    :param profile:
    :return: A list of ProfileSection objects.
    """
    sections = []
    conf_updater = profile.bundle_config()
    for block in conf_updater.iter_blocks():
        if isinstance(block, cu.Section):
            section_name = block.name
            section_items = []
            for section_block in block.iter_blocks():
                if isinstance(section_block, cu.Space):
                    continue
                if isinstance(section_block, cu.Comment):
                    section_block: cu.Comment
                    comment = str(section_block)
                    comment = comment.replace("#", "").strip().replace("\n", "").strip()
                    section_items.append(ProfileComment(comment))
                    continue
                if isinstance(section_block, cu.Option):
                    section_block: cu.Option
                    key = section_block.key
                    value = section_block.value
                    print("key", key)
                    print("value", value)

            print("items", section_items)

    print("sections", sections)
    return sections


def to_snake_case(name: str) -> str:
    """
    Convert the given name to snake case.

    :param name: The name to convert.
    :return: The converted name.
    """
    # https://stackoverflow.com/a/1176023
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def to_display_name(name: str) -> str:
    """
    Convert the given name to a display name.
    Split on underscores or CamelCase and capitalize each word.

    :param name: The name to convert.
    :return: The converted name.
    """
    name = name.replace("_", " ")
    # https://stackoverflow.com/a/1176023
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1 \2", name)
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1 \2", s1)
    return " ".join(word.capitalize() for word in s2.split(" "))
