from uuid import UUID

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._store: dict[UUID, User] = {}

    def find_by_id(self, user_id: UUID) -> User | None:
        return self._store.get(user_id)

    def find_by_email(self, email: str) -> User | None:
        return next((u for u in self._store.values() if u.email == email), None)

    def find_all(self) -> list[User]:
        return list(self._store.values())

    def save(self, user: User) -> User:
        self._store[user.id] = user
        return user

    def delete(self, user_id: UUID) -> None:
        self._store.pop(user_id, None)
