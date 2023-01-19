from final.model.entity import ReservationPending
from .respository import Repository


class ReservationPendingRepository(Repository):
    def __init__(self):
        super().__init__(ReservationPending)

    def find_all(self) -> list[ReservationPending]:
        sql = """
            SELECT r.id           AS id,
                   r.reservations AS reservations,
                   r.status       AS status,
                   t.name         AS tour_name,
                   o.id           AS offer_id,
                   o.price        AS offer_price,
                   o.starting_at  AS offer_starting_at,
                   o.ending_at    AS offer_ending_at,
                   u.full_name    AS user_full_name,
                   u.phone        AS user_phone
            FROM reservation r
                     JOIN user u on u.id = r.user_id
                     JOIN offer o on o.id = r.offer_id
                     JOIN tour t on o.tour_id = t.id
                     LEFT JOIN review r2 on r2.reservation_id = r.id
            WHERE r.status = 1
            ORDER BY offer_starting_at
        """
        return self._fetchall(sql)
