from fastapi import APIRouter
from controller.book_controller import BookController
from pydantic import BaseModel

router = APIRouter()

class BookRequest(BaseModel):
    name: str
    genre: str
    copies_number: int

book_controller = BookController()

@router.post("/books/")
def add_book(book: BookRequest):
    return book_controller.create(book.name, book.genre, book.copies_number)

@router.get("/getbooks/{book_id}")
def get_book(book_id: int):
    return book_controller.get(book_id)
