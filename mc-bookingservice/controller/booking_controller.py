from models.booking_models import Booking
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BookingController:
    def create_booking(self, start_date, end_date, book_id, user_id):
        db = SessionLocal()
        new_booking = Booking(
            start_date=start_date,
            end_date=end_date,
            book_id=book_id,  # O ID do livro precisa ser válido
            user_id=user_id
        )
        db.add(new_booking)
        db.commit()
        db.refresh(new_booking)
        return new_booking