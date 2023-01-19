from dataclasses import dataclass

from final.model.role import Role


@dataclass
class User:
    id: int
    login: str
    password: str
    full_name: str
    phone: int
    role: Role

    def __post_init__(self):
        self.role = Role.from_id(self.role)
