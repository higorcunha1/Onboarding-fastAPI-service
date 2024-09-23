from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    genre = Column(String)
    copies_number = Column(Integer)

    #bookings = relationship("Booking", back_populates="book")