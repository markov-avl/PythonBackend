from final.model.entity import User
from .respository import Repository


class UserRepository(Repository):
    def __init__(self):
        super().__init__(User)

    def create(self, login: str, password: str, full_name: str, phone: int, role: int) -> User:
        sql = """
            INSERT INTO user (login, password, full_name, phone, role)
            VALUES (?, ?, ?, ?, ?)
        """
        id_ = self._insert(sql, (login, password, full_name, phone, role))
        return self.find_by_id(id_)

    def find_by_id(self, id_: int) -> User | None:
        sql = """
            SELECT u.*
            FROM user u
            WHERE u.id = ?
        """
        return self._fetchone(sql, (id_,))

    def find_by_login(self, login: str) -> User | None:
        sql = """
            SELECT u.*
            FROM user u
            WHERE u.login = ?
        """
        return self._fetchone(sql, (login,))

    def find_by_phone(self, phone: int) -> User | None:
        sql = """
            SELECT u.*
            FROM user u
            WHERE u.phone = ?
        """
        return self._fetchone(sql, (phone,))

    def find_by_login_or_phone_and_password(self, login: str, phone: int, password: str) -> User | None:
        sql = """
            SELECT u.*
            FROM user u
            WHERE (u.login = ? OR u.phone = ?)
              AND u.password = ?
        """
        return self._fetchone(sql, (login, phone, password))
