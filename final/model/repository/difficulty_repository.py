from final.model.entity import Difficulty
from .respository import Repository


class DifficultyRepository(Repository):
    def __init__(self):
        super().__init__(Difficulty)

    def find_all(self) -> list[Difficulty]:
        sql = """
            SELECT d.*
            FROM difficulty d
        """
        return self._fetchall(sql)
