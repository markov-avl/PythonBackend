from final.model.entity import User
from final.model.repository import UserRepository
from final.model.role import Role


class UserService:
    def __init__(self):
        self._user_repository = UserRepository()

    def create(self, login: str, password: str, phone: str, name: str, surname: str, patronymic: str = None) -> User:
        phone = self._build_phone(phone)
        full_name = self._build_full_name(name, surname, patronymic)
        if self.get_by_login(login):
            raise ValueError('Пользователь с таким логином уже существует')
        if self.get_by_phone(phone):
            raise ValueError('Пользователь с таким номером телефона уже существует')
        return self._user_repository.create(login, password, full_name, phone, int(Role.USER))

    def get_by_identifier_and_password(self, identifier: str, password: str) -> User | None:
        try:
            phone = self._build_phone(identifier)
        except ValueError:
            phone = -1
        return self._user_repository.find_by_login_or_phone_and_password(identifier, phone, password)

    def get_by_login(self, login: str) -> User | None:
        return self._user_repository.find_by_login(login)

    def get_by_phone(self, phone: int) -> User | None:
        return self._user_repository.find_by_phone(phone)

    @staticmethod
    def _build_full_name(name: str, surname: str, patronymic: str = None) -> str:
        return ' '.join(part for part in [name, surname, patronymic] if part).title()

    @staticmethod
    def _build_phone(phone_field: str) -> int:
        return int(''.join(s for s in phone_field if s.isdigit()))
