from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.db.main import init_db
from src.books.routes import book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # code that runs at the start of the app
    print("Server is starting")
    await init_db()

    yield
    print("Server is shutting down")
    # code that runs after the app stops


app = FastAPI(
    title="Book Service",
    version="0.1.0",
    description="A simple example of FastAPI application",
    lifespan=lifespan,
)

app.include_router(book_router, tags=["book"])

@app.get("/ping")
async def ping():
    return {"message": "pong"}
