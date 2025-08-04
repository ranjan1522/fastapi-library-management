from fastapi import APIRouter,HTTPException
from models import BorrowRequest
from database import books_db, borrowed_books,members_db
import logging

logging.basicConfig(level=logging.INFO)
router = APIRouter()

@router.post("/borrow")
def borrow_book(request: BorrowRequest):
    logging.info("📥 POST /borrow called")

    book = next((b for b in books_db if b.id == request.book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book ID does not exist")

    member = next((m for m in members_db if m.id == request.member_id), None)
    if not member:
        raise HTTPException(status_code=404, detail="Member ID does not exist")

    if not book.available:
        return {"error": "Book not available"}

    book.available = False
    borrowed_books[book.id] = request.member_id
    return {"message": "Book borrowed"}

@router.post("/return")
def return_book(request: BorrowRequest):
    logging.info("📤 POST /return called")

    if borrowed_books.get(request.book_id) != request.member_id:
        return {"error": "Invalid return"}

    book = next((b for b in books_db if b.id == request.book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found during return")

    book.available = True
    del borrowed_books[book.id]
    return {"message": "Book returned"}
