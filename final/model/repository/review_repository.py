from final.model.entity import Review
from .respository import Repository


class ReviewRepository(Repository):
    def __init__(self):
        super().__init__(Review)

    def find_by_id(self, id_: int) -> Review | None:
        sql = """
            SELECT r.*
            FROM review r
            WHERE r.id = ?
        """
        return self._fetchone(sql, (id_,))

    def create(self, reservation_id: int, rating: int, comment: str) -> Review:
        sql = f"""
            INSERT INTO review (reservation_id, rating, comment, created_at)
            VALUES (?, ?, ?, strftime('%s', 'now') * 1000)
        """
        id_ = self._insert(sql, (reservation_id, rating, comment))
        return self.find_by_id(id_)
