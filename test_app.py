import pytest
from app import app
import json

def test_pytest_works():
    assert 1 + 1 == 2


# Fixture to create a test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask Weather App" in response.data





