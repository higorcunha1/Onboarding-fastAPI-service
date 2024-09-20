from fastapi import APIRouter, Depends
from models import Book
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()


@router.get("/books/")
def list_books(db: Session = Depends(get_db)):
    # Consultar todos os livros na tabela 'books'
    books = db.query(Book).all()
    return {"books": books} 