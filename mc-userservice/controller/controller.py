from fastapi.responses import JSONResponse
from models.models import User
from database import SessionLocal, DatabaseSession

# Function to get the db connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserController:
    def create(self, name: str):
        with DatabaseSession() as db:
            db = next(get_db())  # Connecting with the db
            db_user = User(name=name)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user

def hello_response():
    return JSONResponse(content={"message": "Hello World"})

def echo_response(value: str):
    return JSONResponse(content={"message": f"Received: {value}"})
