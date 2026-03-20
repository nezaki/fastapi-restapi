from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.domain.exceptions.user_exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)


def register_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(UserNotFoundError)
    async def user_not_found_handler(
        request: Request, exc: UserNotFoundError
    ) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(UserAlreadyExistsError)
    async def user_already_exists_handler(
        request: Request, exc: UserAlreadyExistsError
    ) -> JSONResponse:
        return JSONResponse(status_code=409, content={"detail": str(exc)})
