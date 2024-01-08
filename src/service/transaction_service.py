import asyncio
import random

from src.model.transaction_model import BaseTransaction, Transaction
from src.repository.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self) -> None:
        self.__repository = TransactionRepository()

    async def manager_transaction(self, transaction: BaseTransaction) -> None:
        await self.generator_transaction(transaction)

    async def generator_transaction(self, transaction: BaseTransaction) -> None:
        list_transaction = [
            Transaction(
                stock_code=transaction.stock_code[
                    random.randint(0, len(transaction.stock_code) - 1)
                ],
            )
            for _ in range(transaction.amount_of_stocks)
        ]
        await self.save_transaction_all(list_transaction)

    async def save_transaction_all(
        self, transactions: list[Transaction], batch_size: int = 10000
    ) -> None:
        tasks = [
            self.__repository.save_transaction_all(transactions[i : i + batch_size])
            for i in range(0, len(transactions), batch_size)
        ]
        await asyncio.gather(*tasks)
