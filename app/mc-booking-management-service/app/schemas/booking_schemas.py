from pydantic import BaseModel
from datetime import date
from typing import Optional


class BookingBase(BaseModel):
    start_date: date
    end_date: date
    book_id: int
    user_id: Optional[int]

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True 
