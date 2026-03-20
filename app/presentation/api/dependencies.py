from app.application.use_cases.user.create_user import CreateUserUseCase
from app.application.use_cases.user.delete_user import DeleteUserUseCase
from app.application.use_cases.user.get_user import GetUserUseCase
from app.application.use_cases.user.list_users import ListUsersUseCase
from app.application.use_cases.user.update_user import UpdateUserUseCase
from app.infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)

# シングルトンとして共有するリポジトリインスタンス
# SQLAlchemy 導入時はここを SqlAlchemyUserRepository に差し替える
_user_repository = InMemoryUserRepository()


def get_create_user_use_case() -> CreateUserUseCase:
    return CreateUserUseCase(_user_repository)


def get_get_user_use_case() -> GetUserUseCase:
    return GetUserUseCase(_user_repository)


def get_list_users_use_case() -> ListUsersUseCase:
    return ListUsersUseCase(_user_repository)


def get_update_user_use_case() -> UpdateUserUseCase:
    return UpdateUserUseCase(_user_repository)


def get_delete_user_use_case() -> DeleteUserUseCase:
    return DeleteUserUseCase(_user_repository)
