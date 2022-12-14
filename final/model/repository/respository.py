from abc import ABC

from final.db import get_db_connection


class Repository(ABC):
    def __init__(self, entity: type):
        self._entity = entity

    def _fetchone(self, sql: str, parameters: tuple = tuple()) -> any:
        with get_db_connection() as connection:
            data = connection.cursor().execute(sql, parameters).fetchone()
        return self._map_optional(data)

    def _fetchall(self, sql: str, parameters: tuple = tuple()) -> any:
        with get_db_connection() as connection:
            data = connection.cursor().execute(sql, parameters).fetchall()
        return self._map_list(data)

    @staticmethod
    def _insert(sql: str, parameters: tuple = tuple()) -> int:
        with get_db_connection() as connection:
            return connection.cursor().execute(sql, parameters).lastrowid

    def _map_optional(self, data: tuple | None) -> any:
        return self._entity(*data) if data else None

    def _map_list(self, data: list[tuple]) -> list[any]:
        return list(map(lambda args: self._entity(*args), data))
