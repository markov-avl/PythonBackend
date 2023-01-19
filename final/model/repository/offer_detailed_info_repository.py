from final.model.entity import OfferDetailedInfo
from .respository import Repository


class OfferDetailedInfoRepository(Repository):
    def __init__(self):
        super().__init__(OfferDetailedInfo)

    def find_by_id(self, id_: int) -> OfferDetailedInfo | None:
        sql = """
            WITH available_reservations AS (SELECT o.id     AS offer_id,
                                                   o.max_reservations -
                                                   SUM(CASE
                                                           WHEN r.status IN (1, 4)
                                                               THEN r.reservations
                                                           ELSE 0
                                                       END) AS available_reservations
                                            FROM offer o
                                                     LEFT JOIN reservation r on o.id = r.offer_id
                                            GROUP BY o.id),
                 average_ratings AS (SELECT o2.id         AS offer_id,
                                            AVG(r.rating) AS rating
                                     FROM review r
                                              JOIN reservation r2 on r2.id = r.reservation_id
                                              JOIN offer o on o.id = r2.offer_id
                                              JOIN tour t on t.id = o.tour_id
                                              JOIN offer o2 on o2.tour_id = t.id
                                     GROUP BY o2.id)
            SELECT o.id,
                   t.name,
                   t.description,
                   r.name || ', ' || m.name,
                   m.height,
                   r2.name,
                   GROUP_CONCAT(t2.name, ", "),
                   d.name,
                   d.rating,
                   d.color,
                   ar.rating,
                   o.starting_at,
                   o.ending_at,
                   o.price,
                   o.max_reservations,
                   ar2.available_reservations
            FROM offer o
                     JOIN tour t on t.id = o.tour_id
                     JOIN tour_tag tt on tt.tour_id = t.id
                     JOIN tag t2 on t2.id = tt.tag_id
                     JOIN mountain m on m.id = t.mountain_id
                     JOIN region r on r.id = m.region_id
                     JOIN region r2 on r2.id = t.starting_point_id
                     JOIN difficulty d on d.id = t.difficulty_id
                     LEFT JOIN average_ratings ar on ar.offer_id = o.id
                     JOIN available_reservations ar2 on ar2.offer_id = o.id
            WHERE o.id = ?
            GROUP BY o.id
        """
        return self._fetchone(sql, (id_,))
