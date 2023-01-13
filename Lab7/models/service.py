from abc import ABC

from Lab7 import database


class Service(ABC):
    @staticmethod
    def _fetchone(sql: str, parameters: tuple = tuple()) -> any:
        with database.get_connection() as connection:
            return connection.cursor().execute(sql, parameters).fetchone()

    @staticmethod
    def _fetchall(sql: str, parameters: tuple = tuple()) -> any:
        with database.get_connection() as connection:
            return connection.cursor().execute(sql, parameters).fetchall()

    @staticmethod
    def _insert(sql: str, parameters: tuple = tuple()) -> int:
        with database.get_connection() as connection:
            return connection.cursor().execute(sql, parameters).lastrowid

    @staticmethod
    def _update(sql: str, parameters: tuple = tuple()) -> None:
        with database.get_connection() as connection:
            connection.cursor().execute(sql, parameters)
