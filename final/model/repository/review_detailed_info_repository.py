from final.model.entity import ReviewDetailedInfo
from .respository import Repository


class ReviewDetailedInfoRepository(Repository):
    def __init__(self):
        super().__init__(ReviewDetailedInfo)

    def find_by_offer_id_ordered_by_created_at_desc(self, offer_id: int) -> list[ReviewDetailedInfo]:
        sql = f"""
            SELECT r.id,
                   r.rating,
                   u.full_name,
                   r.comment,
                   r.created_at
            FROM review r
                     JOIN reservation r2 on r2.id = r.reservation_id
                     JOIN user u on u.id = r2.user_id
                     JOIN offer o on o.id = r2.offer_id
                     JOIN tour t on t.id = o.tour_id
                     JOIN offer o2 on o2.tour_id = t.id
            WHERE o2.id = ?
            ORDER BY r.created_at DESC
        """
        return self._fetchall(sql, (offer_id,))
