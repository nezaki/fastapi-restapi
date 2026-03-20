from uuid import UUID

from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    name: str
    email: str


class UserUpdateRequest(BaseModel):
    name: str | None = None
    email: str | None = None


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: str
