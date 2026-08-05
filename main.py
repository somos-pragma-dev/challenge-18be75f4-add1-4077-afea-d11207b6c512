from fastapi import FastAPI
from app.api.transaction import router as transaction_router

app = FastAPI()

app.include_router(transaction_router)