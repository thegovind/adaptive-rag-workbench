import pytest
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.main import app

class TestAppConfiguration:
    def test_app_is_fastapi_instance(self):
        assert isinstance(app, FastAPI)
    
    def test_app_title_and_version(self):
        assert app.title == "Adaptive RAG Workbench"
        assert app.version == "1.0.0"
    
    def test_cors_middleware_configured(self):
        middleware_classes = [middleware.cls for middleware in app.user_middleware]
        assert CORSMiddleware in middleware_classes
    
    def test_cors_middleware_settings(self):
        cors_middleware = None
        for middleware in app.user_middleware:
            if middleware.cls == CORSMiddleware:
                cors_middleware = middleware
                break
        
        assert cors_middleware is not None
        assert cors_middleware.kwargs["allow_origins"] == ["*"]
        assert cors_middleware.kwargs["allow_credentials"] is True
        assert cors_middleware.kwargs["allow_methods"] == ["*"]
        assert cors_middleware.kwargs["allow_headers"] == ["*"]
    
    def test_routes_registered(self):
        routes = [route.path for route in app.routes]
        assert "/healthz" in routes
        assert "/" in routes
        assert any(route.startswith("/api") for route in routes)
    
    def test_lifespan_configured(self):
        assert app.router.lifespan_context is not None
