from src.infra.database import get_session_maker, Transaction


class TransactionRepository:
    def __init__(self):
        self.sessionmaker = get_session_maker()

    async def save_transaction(self, transaction: Transaction):
        async with self.sessionmaker() as session:
            async with session.begin():
                save = Transaction(
                    stock_code=transaction.stock_code,
                    value=transaction.value,
                    created_at=transaction.created_at,
                )
                session.add(save)
                await session.commit()

        return transaction
