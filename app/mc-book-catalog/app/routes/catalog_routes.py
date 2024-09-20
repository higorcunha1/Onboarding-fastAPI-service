from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controller.catalog_controller import list_books, delete_book

router = APIRouter()

@router.get("/books/")
def list_books_route(db: Session = Depends(get_db)):
    books = list_books(db)
    return {"books": books}

@router.delete("/book-delete/{book_id}", response_model=str)
def delete_book_route(book_id: int, db: Session = Depends(get_db)):
    return delete_book(book_id, db)
