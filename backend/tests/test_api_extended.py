import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAPIEndpoints:
    def test_healthz_endpoint_detailed(self):
        response = client.get("/healthz")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
        assert response.headers["content-type"] == "application/json"
    
    def test_root_endpoint_detailed(self):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert data["message"] == "Adaptive RAG Workbench API"
        assert data["version"] == "1.0.0"
    
    def test_cors_headers_with_origin(self):
        response = client.get("/healthz", headers={"Origin": "http://localhost:3000"})
        assert response.status_code == 200
        assert "access-control-allow-origin" in response.headers
        assert response.headers["access-control-allow-origin"] == "*"
    
    def test_cors_preflight_request(self):
        response = client.options("/healthz", headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "GET"
        })
        assert response.status_code == 200
        assert "access-control-allow-origin" in response.headers
        assert "access-control-allow-methods" in response.headers
    
    def test_nonexistent_endpoint(self):
        response = client.get("/nonexistent")
        assert response.status_code == 404

class TestAPIRouterIntegration:
    def test_api_prefix_routes_exist(self):
        response = client.get("/api/index-stats")
        assert response.status_code == 200
        data = response.json()
        assert "total_documents" in data
        assert "company_breakdown" in data
