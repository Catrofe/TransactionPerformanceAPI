from typing import Optional

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.infra.database import create_database
from src.routes import transaction_routes as transaction_router

app = FastAPI()

BASE_PATH = "/api/transaction"


@app.on_event("startup")
async def startup_event(url: Optional[str] = None) -> None:
    await create_database(url)


@app.get("/")
async def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse(url="/docs")


app.include_router(transaction_router.router, prefix=BASE_PATH, tags=["Transaction"])
