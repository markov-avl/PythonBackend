from final.model.entity import Tag
from .respository import Repository


class TagRepository(Repository):
    def __init__(self):
        super().__init__(Tag)
