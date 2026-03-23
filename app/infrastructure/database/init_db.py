from app.infrastructure.database.base import Base
from app.infrastructure.database.models.user_model import UserModel  # noqa: F401
from app.infrastructure.database.session import engine


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
