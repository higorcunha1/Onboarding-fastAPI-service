from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.controller.controller import hello_response, echo_response
from sqlalchemy.orm import Session
from app.controller.controller import create_user, create_book, create_booking
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/")
def add_user(name: str, db: Session = Depends(get_db)):
    return create_user(db, name)

@router.post("/books/")
def add_book(name: str, genre: str, copies_number: int, db: Session = Depends(get_db)):
    return create_book(db, name, genre, copies_number)

@router.post("/bookings/")
def add_booking(start_date: str, end_date: str, book_id: int, user_id: int, db: Session = Depends(get_db)):
    return create_booking(db, start_date, end_date, book_id, user_id)


@router.get("/hello") # hello world route (GET)
async def hello_world():
    return hello_response()

class EchoRequest(BaseModel): # data model for the POST request
    value: str

@router.post("/echo") # Echo route (POST)
async def echo(request: EchoRequest):
    return echo_response(request.value)