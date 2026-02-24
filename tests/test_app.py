import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    # Можно добавить дополнительные проверки содержимого ответа, если известно, что возвращает корень
    # assert response.json() == {"message": "Hello World"}
