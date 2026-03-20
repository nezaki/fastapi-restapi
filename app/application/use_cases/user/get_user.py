from uuid import UUID

from app.application.dto.user_dto import UserResponseDTO
from app.domain.exceptions.user_exceptions import UserNotFoundError
from app.domain.repositories.user_repository import UserRepository


class GetUserUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def execute(self, user_id: UUID) -> UserResponseDTO:
        user = self._repository.find_by_id(user_id)
        if user is None:
            raise UserNotFoundError(user_id)
        return UserResponseDTO(id=user.id, name=user.name, email=user.email)
