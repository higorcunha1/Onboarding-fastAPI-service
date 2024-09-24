from fastapi import APIRouter
from controller.booking_controller import BookingController
from pydantic import BaseModel

router = APIRouter()

class BookingRequest(BaseModel):
    start_date: str
    end_date: str
    book_id: int
    user_id: int

booking_controller = BookingController()

@router.post("/bookings/")
def add_booking(booking: BookingRequest):
    return booking_controller.create_booking(booking.start_date, booking.end_date, booking.book_id, booking.user_id)
