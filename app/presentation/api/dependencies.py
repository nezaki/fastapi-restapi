from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.use_cases.user.create_user import CreateUserUseCase
from app.application.use_cases.user.delete_user import DeleteUserUseCase
from app.application.use_cases.user.get_user import GetUserUseCase
from app.application.use_cases.user.list_users import ListUsersUseCase
from app.application.use_cases.user.update_user import UpdateUserUseCase
from app.infrastructure.database.session import get_db_session
from app.infrastructure.repositories.mysql_user_repository import MySQLUserRepository


def get_user_repository(
    session: Session = Depends(get_db_session),
) -> MySQLUserRepository:
    return MySQLUserRepository(session)


def get_create_user_use_case(
    repo: MySQLUserRepository = Depends(get_user_repository),
) -> CreateUserUseCase:
    return CreateUserUseCase(repo)


def get_get_user_use_case(
    repo: MySQLUserRepository = Depends(get_user_repository),
) -> GetUserUseCase:
    return GetUserUseCase(repo)


def get_list_users_use_case(
    repo: MySQLUserRepository = Depends(get_user_repository),
) -> ListUsersUseCase:
    return ListUsersUseCase(repo)


def get_update_user_use_case(
    repo: MySQLUserRepository = Depends(get_user_repository),
) -> UpdateUserUseCase:
    return UpdateUserUseCase(repo)


def get_delete_user_use_case(
    repo: MySQLUserRepository = Depends(get_user_repository),
) -> DeleteUserUseCase:
    return DeleteUserUseCase(repo)
