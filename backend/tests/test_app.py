import pytest
from fastapi import FastAPI
from app.main import app

class TestAppConfiguration:
    def test_app_is_fastapi_instance(self):
        assert isinstance(app, FastAPI)
    
    def test_cors_middleware_configured(self):
        middleware_classes = [middleware.cls for middleware in app.user_middleware]
        from fastapi.middleware.cors import CORSMiddleware
        assert CORSMiddleware in middleware_classes
    
    def test_health_endpoint_registered(self):
        routes = [route.path for route in app.routes]
        assert "/healthz" in routes
