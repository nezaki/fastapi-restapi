from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.application.dto.user_dto import CreateUserDTO, UpdateUserDTO
from app.application.use_cases.user.create_user import CreateUserUseCase
from app.application.use_cases.user.delete_user import DeleteUserUseCase
from app.application.use_cases.user.get_user import GetUserUseCase
from app.application.use_cases.user.list_users import ListUsersUseCase
from app.application.use_cases.user.update_user import UpdateUserUseCase
from app.presentation.api.dependencies import (
    get_create_user_use_case,
    get_delete_user_use_case,
    get_get_user_use_case,
    get_list_users_use_case,
    get_update_user_use_case,
)
from app.presentation.schemas.user_schemas import (
    UserCreateRequest,
    UserResponse,
    UserUpdateRequest,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    body: UserCreateRequest,
    use_case: CreateUserUseCase = Depends(get_create_user_use_case),
) -> UserResponse:
    result = use_case.execute(CreateUserDTO(name=body.name, email=body.email))
    return UserResponse(id=result.id, name=result.name, email=result.email)


@router.get("/", response_model=list[UserResponse])
def list_users(
    use_case: ListUsersUseCase = Depends(get_list_users_use_case),
) -> list[UserResponse]:
    results = use_case.execute()
    return [UserResponse(id=r.id, name=r.name, email=r.email) for r in results]


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: UUID,
    use_case: GetUserUseCase = Depends(get_get_user_use_case),
) -> UserResponse:
    result = use_case.execute(user_id)
    return UserResponse(id=result.id, name=result.name, email=result.email)


@router.patch("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: UUID,
    body: UserUpdateRequest,
    use_case: UpdateUserUseCase = Depends(get_update_user_use_case),
) -> UserResponse:
    result = use_case.execute(user_id, UpdateUserDTO(name=body.name, email=body.email))
    return UserResponse(id=result.id, name=result.name, email=result.email)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: UUID,
    use_case: DeleteUserUseCase = Depends(get_delete_user_use_case),
) -> None:
    use_case.execute(user_id)
