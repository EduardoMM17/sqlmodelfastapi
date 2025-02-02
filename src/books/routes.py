from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from http import HTTPStatus

from src.db.main import get_session

book_router = APIRouter(prefix="/books")

@book_router.get("/")
async def read_books(session: AsyncSession = Depends(get_session)):
    pass

@book_router.post("/", status_code=HTTPStatus.CREATED)
async def create_book(session: AsyncSession = Depends(get_session)):
    pass

@book_router.get("/{book_id}", status_code=HTTPStatus.OK)
async def read_book(book_id: str, session: AsyncSession=Depends(get_session)):
    pass

@book_router.put("/{book_id}", status_code=HTTPStatus.OK)
async def update_book(book_id: str, session: AsyncSession=Depends(get_session)):
    pass

@book_router.delete("/{book_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_book(book_id: str, session: AsyncSession=Depends(get_session)):
    pass