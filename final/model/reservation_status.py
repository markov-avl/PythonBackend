from __future__ import annotations


class ReservationStatus:
    PAID = 1
    CANCELED = 2
    REFUSED = 3
    ACCEPTED = 4

    def __init__(self, id_: int, name: str, color: str):
        self._id = id_
        self._name = name
        self._color = color

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def color(self) -> str:
        return self._color

    @staticmethod
    def from_id(id_: int) -> ReservationStatus | None:
        return next(filter(lambda role: id_ == role.id, (
            ReservationStatus.PAID,
            ReservationStatus.CANCELED,
            ReservationStatus.REFUSED,
            ReservationStatus.ACCEPTED
        )), None)

    def __int__(self) -> int:
        return self._id

    def __str__(self) -> str:
        return self._name


ReservationStatus.PAID = ReservationStatus(1, 'Оплачено', 'primary')
ReservationStatus.CANCELED = ReservationStatus(2, 'Отменено', 'secondary')
ReservationStatus.REFUSED = ReservationStatus(3, 'Отклонено', 'danger')
ReservationStatus.ACCEPTED = ReservationStatus(4, 'Подтверждено', 'success')
