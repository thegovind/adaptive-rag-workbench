import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestHealthEndpoint:
    def test_health_check_returns_200(self):
        response = client.get("/healthz")
        assert response.status_code == 200
    
    def test_health_check_returns_correct_json(self):
        response = client.get("/healthz")
        assert response.json() == {"status": "ok"}
    
    def test_health_check_content_type(self):
        response = client.get("/healthz")
        assert response.headers["content-type"] == "application/json"

class TestCORSMiddleware:
    def test_cors_headers_present(self):
        response = client.get("/healthz", headers={"Origin": "http://localhost:3000"})
        assert "access-control-allow-origin" in response.headers
        assert response.headers["access-control-allow-origin"] == "*"
