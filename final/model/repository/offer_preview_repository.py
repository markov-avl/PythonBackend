from final.model.entity import OfferPreview
from .respository import Repository


class OfferPreviewRepository(Repository):
    def __init__(self):
        super().__init__(OfferPreview)

    def find_all(self,
                 search: str = None,
                 tags: list[int] = None,
                 difficulties: list[int] = None,
                 min_rating: int = None,
                 max_price: float = None,
                 min_available_reservations: int = None) -> list[OfferPreview]:
        filters = [
            "datetime(o.starting_at / 1000, 'unixepoch') > date('now', '+1 day')",
            "ar2.available_reservations > 0",
            "o.id IN tagged_offers"
        ]
        if search:
            filters.append(f"LOWER(t.name) LIKE '%{search.lower()}%'")
        if difficulties:
            filters.append(f"d.id IN ({', '.join(map(str, difficulties))})")
        if min_rating:
            filters.append(f"(ar.rating >= {min_rating} OR ar.rating IS NULL)")
        if max_price:
            filters.append(f"o.price <= {max_price}")
        if min_available_reservations:
            filters.append(f"ar2.available_reservations >= {min_available_reservations}")

        sql = f"""
            WITH tagged_offers AS (SELECT o.id AS offer_id
                                   FROM offer o
                                            JOIN tour t on t.id = o.tour_id
                                            JOIN tour_tag tt on tt.tour_id = t.id
                                   {f"WHERE tt.tag_id IN ({', '.join(map(str, tags))})" if tags else ''}
                                   GROUP BY o.id),
                 available_reservations AS (SELECT o.id     AS offer_id,
                                                   o.max_reservations -
                                                   SUM(CASE
                                                           WHEN r.status = 1
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
                   r.name || ', ' || m.name,
                   GROUP_CONCAT(t2.name, ", "),
                   d.name,
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
                     JOIN difficulty d on d.id = t.difficulty_id
                     LEFT JOIN average_ratings ar on ar.offer_id = o.id
                     JOIN available_reservations ar2 on ar2.offer_id = o.id
            WHERE {' AND '.join(filters)}
            GROUP BY o.id
        """
        return self._fetchall(sql)
