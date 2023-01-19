from final.model.entity import Reservation
from .respository import Repository


class ReservationRepository(Repository):
    def __init__(self):
        super().__init__(Reservation)

    def find_by_id(self, id_: int) -> Reservation | None:
        sql = """
            SELECT r.*
            FROM reservation r
            WHERE r.id = ?
        """
        return self._fetchone(sql, (id_,))

    def create(self, offer_id: int, user_id: int, reservations: int, status: int) -> Reservation:
        sql = """
            INSERT INTO reservation (offer_id, user_id, reservations, status)
            VALUES (?, ?, ?, ?)
        """
        id_ = self._insert(sql, (offer_id, user_id, reservations, status))
        return self.find_by_id(id_)

    def update_status(self, id_: int, status: int) -> None:
        sql = """
            UPDATE reservation
            SET status = ?
            WHERE id = ?
        """
        self._execute(sql, (status, id_))
