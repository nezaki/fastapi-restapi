from app.application.dto.user_dto import CreateUserDTO, UserResponseDTO
from app.domain.entities.user import User
from app.domain.exceptions.user_exceptions import UserAlreadyExistsError
from app.domain.repositories.user_repository import UserRepository


class CreateUserUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def execute(self, dto: CreateUserDTO) -> UserResponseDTO:
        if self._repository.find_by_email(dto.email):
            raise UserAlreadyExistsError(dto.email)
        user = User(name=dto.name, email=dto.email)
        saved = self._repository.save(user)
        return UserResponseDTO(id=saved.id, name=saved.name, email=saved.email)
