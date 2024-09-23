import requests
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.booking_models import Booking
from database import SessionLocal
from requests.auth import HTTPBasicAuth
import os

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BookingController:
    def check_book_availability(self, book_id: int):
        # URL do microsserviço de catálogo
        url = f"http://book-service:8001/getbooks/{book_id}"  # Usando f-string para formatar a URL

        # Adicione suas credenciais aqui
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')

        response = requests.get(url, auth=HTTPBasicAuth(username, password))
            
        # Faz a requisição ao microsserviço de catálogo
        response = requests.get(url)
        
        if response.status_code == 200:
            book_data = response.json()
            # Verifica se o número de cópias disponíveis é maior que 0
            if book_data['copies_number'] > 0:
                return book_data
            else:
                return JSONResponse(status_code=400, content={"detail": "No copies available"})
        else:
            return JSONResponse(status_code=404, content={"detail": "Book not found"})

    def create(self, start_date: str, end_date: str, book_id: int, user_id: int):
        db = next(get_db())  # Conectar ao banco de dados
        
        # Verifica a disponibilidade do livro antes de criar a reserva
        book_data = self.check_book_availability(book_id)
        if isinstance(book_data, JSONResponse):
            # Retorna o erro se o livro não estiver disponível
            return book_data
        
        # Se o livro estiver disponível, cria a reserva
        db_booking = Booking(start_date=start_date, end_date=end_date, book_id=book_id, user_id=user_id)
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking
