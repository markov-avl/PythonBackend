from dataclasses import dataclass


@dataclass
class User:
    id: int
    login: str
    password: str
    full_name: str
    phone: int
    role: int
