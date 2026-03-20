from uuid import UUID

from app.application.dto.user_dto import UpdateUserDTO, UserResponseDTO
from app.domain.exceptions.user_exceptions import UserNotFoundError
from app.domain.repositories.user_repository import UserRepository


class UpdateUserUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def execute(self, user_id: UUID, dto: UpdateUserDTO) -> UserResponseDTO:
        user = self._repository.find_by_id(user_id)
        if user is None:
            raise UserNotFoundError(user_id)
        if dto.name is not None:
            user.name = dto.name
        if dto.email is not None:
            user.change_email(dto.email)
        saved = self._repository.save(user)
        return UserResponseDTO(id=saved.id, name=saved.name, email=saved.email)
