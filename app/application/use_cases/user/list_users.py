from app.application.dto.user_dto import UserResponseDTO
from app.domain.repositories.user_repository import UserRepository


class ListUsersUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def execute(self) -> list[UserResponseDTO]:
        users = self._repository.find_all()
        return [UserResponseDTO(id=u.id, name=u.name, email=u.email) for u in users]
