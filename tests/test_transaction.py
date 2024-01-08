import asyncio

import pytest
from fastapi.testclient import TestClient

from src.app import app, startup_event

client = TestClient(app)

URL_API = "/api/transaction"


@pytest.fixture
def change_db_url():
    asyncio.run(startup_event("sqlite+aiosqlite:///transaction_db.db"))


def test_create_transaction(change_db_url):
    response = client.post(
        URL_API,
        json={"stock_code": ["PETR4"], "amount_of_stocks": 1},
    )
    assert response.status_code == 201
