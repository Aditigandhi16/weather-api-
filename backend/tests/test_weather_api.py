import pytest
from fastapi.testclient import TestClient
from app.main import app
import logging

client = TestClient(app)

logger = logging.getLogger()

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Weather API"}
    logger.info("Root test passed")

def test_get_weather():
    response = client.get("/api/v1/weather-by-ip?ip=8.8.8.8")
    assert response.status_code == 200
    assert "weather" in response.json()
    logger.info("Weather test passed")
