from fastapi import FastAPI
from routers import books, members, transactions
import logging

logging.basicConfig(level=logging.INFO)
logging.info("✅ App started and loading routers")

app = FastAPI()

app.include_router(books.router)
app.include_router(members.router)
app.include_router(transactions.router)