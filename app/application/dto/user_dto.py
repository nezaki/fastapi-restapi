from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateUserDTO:
    name: str
    email: str


@dataclass
class UpdateUserDTO:
    name: str | None = None
    email: str | None = None


@dataclass
class UserResponseDTO:
    id: UUID
    name: str
    email: str
