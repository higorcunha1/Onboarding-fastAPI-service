from fastapi.responses import JSONResponse
from models.book_models import Book
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BookController:
    def create(self, name: str, genre: str, copies_number: int):
        db = next(get_db())  # Conectar ao banco de dados
        db_book = Book(name=name, genre=genre, copies_number=copies_number)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

    def get(self, book_id: int):
            db = next(get_db())
            book = db.query(Book).filter(Book.id == book_id).first()
            if book:
                return book
            else:
                return JSONResponse(status_code=404, content={"detail": "Book not found"})
