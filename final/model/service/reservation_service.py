from final.model.entity import Reservation, ReservationDetailedInfo, ReservationPending
from final.model.repository import ReservationRepository, ReservationDetailedInfoRepository, \
    ReservationPendingRepository
from final.model.reservation_status import ReservationStatus


class ReservationService:
    def __init__(self):
        self._reservation_repository = ReservationRepository()
        self._reservation_detailed_info_repository = ReservationDetailedInfoRepository()
        self._reservation_pending_repository = ReservationPendingRepository()

    def create(self, offer_id: int, user_id: int, reservations: int = 1) -> Reservation:
        return self._reservation_repository.create(offer_id, user_id, reservations, int(ReservationStatus.PAID))

    def get_detailed_info_by_user_id(self, user_id: int) -> list[ReservationDetailedInfo]:
        return self._reservation_detailed_info_repository.find_by_user_id(user_id)

    def get_pending(self) -> list[ReservationPending]:
        return self._reservation_pending_repository.find_all()

    def update_status(self, reservation_id: int, status: ReservationStatus) -> None:
        return self._reservation_repository.update_status(reservation_id, int(status))
