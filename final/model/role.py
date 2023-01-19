from __future__ import annotations


class Role:
    __slots__ = [
        '_id',
        '_name',
        'USER',
        'ADMIN'
    ]

    def __init__(self, id_: int, name: str):
        self._id = id_
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @staticmethod
    def from_id(id_: int) -> Role | None:
        return next(filter(lambda role: id_ == role.id, (Role.USER, Role.ADMIN)), None)

    def __int__(self) -> int:
        return self._id

    def __str__(self) -> str:
        return self._name


Role.USER = Role(1, 'Пользователь')
Role.ADMIN = Role(2, 'Администратор')
