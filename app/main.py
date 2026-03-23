from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.infrastructure.database.init_db import init_db
from app.presentation.api.error_handlers import register_error_handlers
from app.presentation.api.v1.router import v1_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    init_db()
    yield


app = FastAPI(
    title="FastAPI REST API",
    version="0.1.0",
    lifespan=lifespan,
)

register_error_handlers(app)
app.include_router(v1_router, prefix="/api")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello, World!"}
