from uuid import UUID

from app.domain.exceptions.user_exceptions import UserNotFoundError
from app.domain.repositories.user_repository import UserRepository


class DeleteUserUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def execute(self, user_id: UUID) -> None:
        if self._repository.find_by_id(user_id) is None:
            raise UserNotFoundError(user_id)
        self._repository.delete(user_id)
