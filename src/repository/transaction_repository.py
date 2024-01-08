from src.infra.database import Transaction, get_session_maker
from src.model.transaction_model import Transaction as TransactionModel


class TransactionRepository:
    def __init__(self) -> None:
        self.sessionmaker = get_session_maker()

    async def save_transaction_all(self, transactions: list[TransactionModel]) -> None:
        async with self.sessionmaker() as session:
            async with session.begin():
                save = [
                    Transaction(
                        stock_code=transaction.stock_code,
                        value=transaction.value,
                        created_at=transaction.created_at,
                    )
                    for transaction in transactions
                ]
                session.add_all(save)
                await session.commit()
