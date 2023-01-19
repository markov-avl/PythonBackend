import datetime
from dataclasses import dataclass

from final.model.reservation_status import ReservationStatus


@dataclass
class ReservationPending:
    id: int
    reservations: int
    status: ReservationStatus
    tour_name: str
    offer_id: int
    offer_price: float
    offer_starting_at: datetime.datetime
    offer_ending_at: datetime.datetime
    user_full_name: str
    user_phone: int

    def __post_init__(self):
        self.status = ReservationStatus.from_id(self.status)
        self.offer_starting_at = datetime.datetime.fromtimestamp(self.offer_starting_at // 1000)
        self.offer_ending_at = datetime.datetime.fromtimestamp(self.offer_ending_at // 1000)
