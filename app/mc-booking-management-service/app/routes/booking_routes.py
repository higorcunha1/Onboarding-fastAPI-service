from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from booking_models import Booking as BookingModel
from schemas.booking_schemas import Booking
from controller.booking_controller import get_all_bookings, delete_booking

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/bookings/", response_model=List[Booking]) 
def get_all_bookings_route(db: Session = Depends(get_db)):
    return get_all_bookings(db)

@router.delete("/booking-delete/{booking_id}", response_model=str)
def delete_booking_route(booking_id: int, db: Session = Depends(get_db)):
    return delete_booking(booking_id, db)