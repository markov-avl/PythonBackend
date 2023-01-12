from dataclasses import dataclass

from .tag import Tag


@dataclass
class TagCounter(Tag):
    count: int
