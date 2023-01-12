import datetime
from dataclasses import dataclass


@dataclass
class OfferPreview:
    id: int
    name: str
    mountain: str
    tags: str
    difficulty: str
    difficulty_color: str
    rating: float | None
    starting_at: datetime.datetime
    ending_at: datetime.datetime
    price: float
    max_reservations: int
    available_reservations: int

    def __post_init__(self):
        self.starting_at = datetime.datetime.fromtimestamp(self.starting_at // 1000)
        self.ending_at = datetime.datetime.fromtimestamp(self.ending_at // 1000)
