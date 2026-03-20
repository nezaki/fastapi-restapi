from fastapi import FastAPI

from app.presentation.api.error_handlers import register_error_handlers
from app.presentation.api.v1.router import v1_router

app = FastAPI(
    title="FastAPI REST API",
    version="0.1.0",
)

register_error_handlers(app)
app.include_router(v1_router, prefix="/api")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello, World!"}
