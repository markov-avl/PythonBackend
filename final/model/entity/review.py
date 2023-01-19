import datetime
from dataclasses import dataclass


@dataclass
class Review:
    id: int
    reservation_id: int
    rating: int
    comment: str
    created_at: datetime.datetime

    def __post_init__(self):
        self.created_at = datetime.datetime.fromtimestamp(self.created_at // 1000)
