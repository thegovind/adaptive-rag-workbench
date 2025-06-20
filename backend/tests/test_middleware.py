import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestMiddleware:
    def test_cors_middleware_allows_all_origins(self):
        response = client.get("/healthz", headers={"Origin": "https://example.com"})
        assert response.status_code == 200
        assert response.headers.get("access-control-allow-origin") == "*"
    
    def test_cors_middleware_allows_credentials(self):
        response = client.get("/healthz", headers={"Origin": "https://example.com"})
        assert response.status_code == 200
        assert response.headers.get("access-control-allow-credentials") == "true"
    
    def test_cors_middleware_preflight_options(self):
        response = client.options("/healthz", headers={
            "Origin": "https://example.com",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "Content-Type"
        })
        assert response.status_code == 200
        assert "access-control-allow-origin" in response.headers
        assert "access-control-allow-methods" in response.headers
        assert "access-control-allow-headers" in response.headers
    
    def test_cors_middleware_actual_request(self):
        response = client.post("/healthz", 
                             headers={"Origin": "https://example.com", "Content-Type": "application/json"},
                             json={})
        assert "access-control-allow-origin" in response.headers
