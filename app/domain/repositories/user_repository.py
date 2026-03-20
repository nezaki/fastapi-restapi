from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: UUID) -> User | None: ...

    @abstractmethod
    def find_by_email(self, email: str) -> User | None: ...

    @abstractmethod
    def find_all(self) -> list[User]: ...

    @abstractmethod
    def save(self, user: User) -> User: ...

    @abstractmethod
    def delete(self, user_id: UUID) -> None: ...
