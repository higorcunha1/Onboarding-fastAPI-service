from fastapi import FastAPI
from routes.booking_routes import router as booking_router

app = FastAPI()

app.include_router(booking_router)
