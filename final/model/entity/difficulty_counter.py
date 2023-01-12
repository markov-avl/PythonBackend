from dataclasses import dataclass

from .difficulty import Difficulty


@dataclass
class DifficultyCounter(Difficulty):
    count: int
