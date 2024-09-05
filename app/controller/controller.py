from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.models.models import User, Book, Booking

def hello_response():
    return JSONResponse(content={"message": "Hello World"})

def echo_response(value: str):
    return JSONResponse(content={"message": f"Received: {value}"})

def create_user(db: Session, name: str):
    db_user = User(name=name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_book(db: Session, name: str, genre: str, copies_number: int):
    db_book = Book(name=name, genre=genre, copies_number=copies_number)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def create_booking(db: Session, start_date: str, end_date: str, book_id: int, user_id: int):
    db_booking = Booking(start_date=start_date, end_date=end_date, book_id=book_id, user_id=user_id)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking