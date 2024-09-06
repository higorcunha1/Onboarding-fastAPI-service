from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.models.models import User, Book, Booking
from app.database import SessionLocal, DatabaseSession

# Function to get the db connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserController:
    def create(self, name: str):
        with DatabaseSession() as db:
            db = next(get_db())  # Connecting with the db
            db_user = User(name=name)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user

class BookController:
    def create(self, name: str, genre: str, copies_number: int):
        db = next(get_db()) # Connecting with the db
        db_book = Book(name=name, genre=genre, copies_number=copies_number)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

class BookingController:
    def create(self, start_date: str, end_date: str, book_id: int, user_id: int):
        db = next(get_db()) # Connecting with the db
        db_booking = Booking(start_date=start_date, end_date=end_date, book_id=book_id, user_id=user_id)
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking

def hello_response():
    return JSONResponse(content={"message": "Hello World"})

def echo_response(value: str):
    return JSONResponse(content={"message": f"Received: {value}"})
