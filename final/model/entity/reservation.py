from dataclasses import dataclass

from final.model.reservation_status import ReservationStatus


@dataclass
class Reservation:
    id: int
    offer_id: int
    user_id: int
    reservations: int
    status: ReservationStatus

    def __post_init__(self):
        self.status = ReservationStatus.from_id(self.status)
