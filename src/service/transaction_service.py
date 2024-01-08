import random

from src.model.transaction_model import BaseTransaction, Transaction
from src.repository.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self) -> None:
        self.__repository = TransactionRepository()

    async def save_transaction(self, transaction: Transaction) -> None:
        await self.__repository.save_transaction(transaction)

    async def manager_transaction(self, transaction: BaseTransaction) -> None:
        for i in range(transaction.amount_of_stocks):
            await self.save_transaction(
                await self.generator_transaction(
                    transaction.stock_code[
                        random.randint(0, len(transaction.stock_code) - 1)
                    ]
                )
            )

    async def generator_transaction(self, stock_code: str) -> Transaction:
        return Transaction(stock_code=stock_code)
