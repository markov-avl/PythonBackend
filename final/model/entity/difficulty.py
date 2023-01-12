from dataclasses import dataclass


@dataclass
class Difficulty:
    id: int
    name: str
    rating: int
    color: str