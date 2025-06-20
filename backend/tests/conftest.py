import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_health_response():
    return {"status": "ok"}

@pytest.fixture
def sample_root_response():
    return {"message": "Adaptive RAG Workbench API", "version": "1.0.0"}

@pytest.fixture
def cors_headers():
    return {"Origin": "http://localhost:3000"}
