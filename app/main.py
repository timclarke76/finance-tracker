"""
Finance Tracker API
A personal finance management system with ML-powered transaction categorization.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient


app = FastAPI(
    title="Finance Tracker API",
    description="Personal finance tracker with ML transaction categorization",
    version="0.1.0",
)

# Enable CORS for frontend (we'll build later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Will restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "message": "Finance Tracker API is running",
        "version": "0.1.0",
        "status": "healthy",
    }


@app.get("/api/v1/transactions")
async def get_transactions():
    """
    Get all transactions.
    TODO: Connect to database in next milestone.
    """
    # Mock data for now
    return {
        "transactions": [
            {
                "id": 1,
                "date": "2025-12-26",
                "description": "Tesco Superstore",
                "amount": -45.32,
                "category": "groceries",  # Will be ML-predicted later
            }
        ]
    }


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Finance Tracker API is running",
        "version": "0.1.0",
        "status": "healthy",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
