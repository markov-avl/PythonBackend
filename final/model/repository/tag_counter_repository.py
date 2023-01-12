from final.model.entity import TagCounter
from .respository import Repository


class TagCounterRepository(Repository):
    def __init__(self):
        super().__init__(TagCounter)

    def find_all(self) -> list[TagCounter]:
        sql = """
            SELECT t.*, COUNT(o.id)
            FROM tag t
                     LEFT JOIN tour_tag tt on t.id = tt.tag_id
                     LEFT JOIN offer o on tt.tour_id = o.tour_id
            GROUP BY t.id
        """
        return self._fetchall(sql)
