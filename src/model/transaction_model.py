import random
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class BaseTransaction(BaseModel):
    stock_code: list[str]
    amount_of_stocks: int


class Transaction(BaseModel):
    id: Optional[int] = None
    stock_code: str
    value: float = round(random.uniform(1, 1001), 2)
    created_at: datetime = datetime.now()