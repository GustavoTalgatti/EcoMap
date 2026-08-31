import os

import pytest
from fastapi.testclient import TestClient

os.environ.setdefault("JWT_SECRET", "test-secret-key-for-pytest-only")

from app.main import app  # noqa: E402


@pytest.fixture
def client():
    return TestClient(app)
