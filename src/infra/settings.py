import os

from pydantic import BaseModel


class Settings(BaseModel):
    db_test: str = "sqlite+aiosqlite:///transaction_db.db"
    db_prod: str = (
        "postgresql+asyncpg://postgres:root@localhost:5432/WatchRecommendation"
    )
    environment: str = (
        str(os.environ.get("ENVIRONMENT")) if os.environ.get("ENVIRONMENT") else "TEST"
    )
