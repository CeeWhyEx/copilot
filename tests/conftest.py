from fastapi.testclient import TestClient
import pytest

from src.app import app, reset_activities
import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activity_data():
    reset_activities()
    yield
    reset_activities()


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def activity_store():
    return app_module.activities