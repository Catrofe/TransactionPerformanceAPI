from fastapi import APIRouter, Depends, HTTPException, status

from src.model.transaction_model import BaseTransaction
from src.service.transaction_service import TransactionService

router = APIRouter()

service = TransactionService()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_transaction(transaction: BaseTransaction) -> None:
    await service.manager_transaction(transaction)