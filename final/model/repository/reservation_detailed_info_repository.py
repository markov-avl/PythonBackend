from final.model.entity import ReservationDetailedInfo
from .respository import Repository


class ReservationDetailedInfoRepository(Repository):
    def __init__(self):
        super().__init__(ReservationDetailedInfo)

    def find_by_user_id(self, user_id: int) -> list[ReservationDetailedInfo]:
        sql = """
            SELECT r.id           AS id,
                   r.reservations AS reservations,
                   r.status       AS status,
                   t.name         AS tour_name,
                   o.id           AS offer_id,
                   o.price        AS offer_price,
                   o.starting_at  AS offer_starting_at,
                   o.ending_at    AS offer_ending_at,
                   r2.comment     AS review_comment,
                   r2.rating      AS review_rating,
                   r2.created_at  AS review_created_at
            FROM reservation r
                     JOIN offer o on o.id = r.offer_id
                     JOIN tour t on o.tour_id = t.id
                     LEFT JOIN review r2 on r2.reservation_id = r.id
            WHERE r.user_id = ?
            ORDER BY offer_starting_at
        """
        return self._fetchall(sql, (user_id,))
