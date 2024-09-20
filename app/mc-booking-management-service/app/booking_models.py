from sqlalchemy import Column, Integer, ForeignKey, Date, String
from database import Base

class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    genre = Column(String)
    copies_number = Column(Integer)
    


