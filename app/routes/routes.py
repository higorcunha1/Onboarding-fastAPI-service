from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import SessionLocal, engine
from app.models.models import User, Book, Booking
from app.controller.controller import hello_response, echo_response
from app.controller.controller import create_user, create_book, create_booking

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    name: str

@router.get("/hello") # hello world route (GET)
async def hello_world():
    return hello_response()

class EchoRequest(BaseModel): # data model for the POST request
    value: str

@router.post("/echo") # Echo route (POST)
async def echo(request: EchoRequest):
    return echo_response(request.value)


@router.post("/users/")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, name=user.name)

class BookCreate(BaseModel):
    name: str
    genre: str
    copies_number: int

@router.post("/books/")
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db=db, **book.dict())

class BookingCreate(BaseModel):
    start_date: str
    end_date: str
    book_id: int
    user_id: int

@router.post("/bookings/")
def add_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    return create_booking(db=db, **booking.dict())