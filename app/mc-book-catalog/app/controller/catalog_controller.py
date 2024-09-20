from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.catalog_models import Book

# Function to list all books from the database
def list_books(db: Session):
    return db.query(Book).all()

# Function to delete a book from the database
def delete_book(book_id: int, db: Session):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return f"Book {book_id} deleted successfully"
