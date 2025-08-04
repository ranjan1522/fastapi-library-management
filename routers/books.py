from fastapi import APIRouter, HTTPException
from models import Book
from database import books_db
import logging

logging.basicConfig(level=logging.INFO)
router = APIRouter(prefix="/books")

@router.get("/")
def get_books():
    logging.info("📚 GET /books/ called")
    return [book.model_dump() for book in books_db]

@router.post("/")
def create_book(book: Book):
    if any(b.id == book.id for b in books_db):
        raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books_db.append(book)
    return {"message": "Book added"}

@router.patch("/{book_id}")
def update_book(book_id: int, updates: dict):
    for book in books_db:
        if book.id == book_id:
            book_data = book.model_dump()
            book_data.update(updates)
            updated = Book(**book_data)
            books_db[books_db.index(book)] = updated
            return {"message": "Book updated", "book": updated}
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{book_id}")
def delete_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            books_db.remove(book)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")