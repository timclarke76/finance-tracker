from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Finance Tracker API is running",
        "version": "0.1.0",
        "status": "healthy",
    }


def test_get_transactions():
    response = client.get("/api/v1/transactions")
    assert response.status_code == 200
    assert response.json() == {
        "transactions": [
            {
                "id": 1,
                "date": "2025-12-26",
                "description": "Tesco Superstore",
                "amount": -45.32,
                "category": "groceries",
            }
        ]
    }

def test_does_not_exist():
    response = client.get("/does/not/exist")
    assert response.status_code == 404
