from final.model.entity import DifficultyCounter
from .respository import Repository


class DifficultyCounterRepository(Repository):
    def __init__(self):
        super().__init__(DifficultyCounter)

    def find_all_ordered_by_rating(self) -> list[DifficultyCounter]:
        sql = """
            SELECT d.*, COUNT(o.id)
            FROM difficulty d
                     LEFT JOIN tour t on d.id = t.difficulty_id
                     LEFT JOIN offer o on t.id = o.tour_id
            GROUP BY d.id
            ORDER BY d.rating
        """
        return self._fetchall(sql)
