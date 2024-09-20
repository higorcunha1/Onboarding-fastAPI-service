from sqlalchemy.orm import Session
from fastapi import HTTPException
from booking_models import Booking as BookingModel, Book
from schemas.booking_schemas import Booking

def get_all_bookings(db: Session):
    return db.query(BookingModel).all()

def delete_booking(booking_id: int, db: Session):
    booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    book = db.query(Book).filter(Book.id == booking.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.copies_number += 1
    db.delete(booking)
    db.commit()
    return f"Booking {booking_id} deleted successfully, stock updated for book {book.id}"
