from final.model.entity import Tag, TagCounter
from final.model.repository import TagRepository, TagCounterRepository


class TagService:
    def __init__(self):
        self._tag_repository = TagRepository()
        self._tag_counter_repository = TagCounterRepository()

    def get_all_with_count(self) -> list[TagCounter]:
        return self._tag_counter_repository.find_all()
