from final.model.entity import Difficulty, DifficultyCounter
from final.model.repository import DifficultyRepository, DifficultyCounterRepository


class DifficultyService:
    def __init__(self):
        self._difficulty_repository = DifficultyRepository()
        self._difficulty_counter_repository = DifficultyCounterRepository()

    def get_all(self) -> list[Difficulty]:
        return self._difficulty_repository.find_all()

    def get_all_with_count_ordered_by_rating(self) -> list[DifficultyCounter]:
        return self._difficulty_counter_repository.find_all_ordered_by_rating()
