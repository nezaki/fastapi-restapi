from uuid import UUID

from sqlalchemy.orm import Session

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.database.models.user_model import UserModel


class MySQLUserRepository(UserRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def find_by_id(self, user_id: UUID) -> User | None:
        model = self._session.get(UserModel, str(user_id))
        return self._to_entity(model) if model else None

    def find_by_email(self, email: str) -> User | None:
        model = self._session.query(UserModel).filter(UserModel.email == email).first()
        return self._to_entity(model) if model else None

    def find_all(self) -> list[User]:
        models = self._session.query(UserModel).all()
        return [self._to_entity(m) for m in models]

    def save(self, user: User) -> User:
        model = self._session.get(UserModel, str(user.id))
        if model:
            model.name = user.name
            model.email = user.email
        else:
            model = UserModel(id=str(user.id), name=user.name, email=user.email)
            self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return self._to_entity(model)

    def delete(self, user_id: UUID) -> None:
        model = self._session.get(UserModel, str(user_id))
        if model:
            self._session.delete(model)
            self._session.commit()

    @staticmethod
    def _to_entity(model: UserModel) -> User:
        return User(id=UUID(model.id), name=model.name, email=model.email)
