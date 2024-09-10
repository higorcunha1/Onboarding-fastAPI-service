from fastapi import APIRouter, Depends
from app.controller.controller import UserController, BookController, BookingController, hello_response, echo_response
from pydantic import BaseModel
from app.auth import authenticate_user
router = APIRouter()

# Defining the request models for the routes
class UserRequest(BaseModel):
    name: str

class BookRequest(BaseModel):
    name: str
    genre: str
    copies_number: int

class BookingRequest(BaseModel):
    start_date: str
    end_date: str
    book_id: int
    user_id: int

# Routes related to users 
user_controller = UserController()

@router.post("/users/")
# Requiring authentication to the route
def add_user(user: UserRequest, username: str = Depends(authenticate_user)):
    return user_controller.create(user.name)

# Routes related to books
book_controller = BookController()

@router.post("/books/")
# Requiring authentication to the route
def add_book(book: BookRequest, username: str = Depends(authenticate_user)):
    return book_controller.create(book.name, book.genre, book.copies_number)

# Routes related to bookings
booking_controller = BookingController()

@router.post("/bookings/")
# Requiring authentication to the route
def add_booking(booking: BookingRequest, username: str = Depends(authenticate_user)):
    return booking_controller.create(booking.start_date, booking.end_date, booking.book_id, booking.user_id)

# Hello world route
@router.get("/hello") 
async def hello_world(username: str = Depends(authenticate_user)):
    return hello_response()

# Echo route
class EchoRequest(BaseModel): 
    value: str

@router.post("/echo") 
async def echo(request: EchoRequest, username: str = Depends(authenticate_user)):
    return echo_response(request.value)
