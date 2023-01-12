import datetime
from dataclasses import dataclass


@dataclass
class ReviewDetailedInfo:
    id: int
    rating: int
    user_full_name: str
    comment: str
    created_at: datetime.datetime

    def __post_init__(self):
        self.created_at = datetime.datetime.fromtimestamp(self.created_at // 1000)
