import pytest
from fastapi.testclient import TestClient

from app.infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from app.main import app
from app.presentation.api import dependencies


@pytest.fixture(autouse=True)
def _fresh_repository():
    """テストごとにリポジトリを初期化してデータを分離する。"""
    repo = InMemoryUserRepository()
    dependencies._user_repository = repo
    yield


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
