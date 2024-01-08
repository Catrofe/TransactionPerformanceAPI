from __future__ import annotations

from datetime import datetime
from typing import Any

from sqlalchemy import DECIMAL, Column, DateTime, Integer, String
from sqlalchemy.ext.asyncio import (  # type: ignore
    AsyncAttrs,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase  # type: ignore

from src.infra.settings import Settings

settings = Settings()


class Base(AsyncAttrs, DeclarativeBase):  # type: ignore
    pass


def get_session_maker() -> Any:
    url = settings.db_prod if settings.environment != "TEST" else settings.db_test
    engine = create_async_engine(
        url,
        echo=False,
    )
    return async_sessionmaker(engine, expire_on_commit=False)


async def create_database() -> None:
    url = settings.db_prod if settings.environment != "TEST" else settings.db_test
    engine = create_async_engine(
        url,
        echo=False,
    )
    if settings.environment == "TEST":
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


class Transaction(Base):
    __tablename__ = "tb_transactions"

    id = Column(Integer, primary_key=True, index=True)
    stock_code = Column(String, nullable=False)
    value = Column(DECIMAL, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
