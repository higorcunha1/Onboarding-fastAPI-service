import uvicorn
from fastapi import FastAPI
from app.routes.routes import router as main_router
from app import app

app = FastAPI()

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(app, host="100.0.0.1", port=8000, reload=True) # running the app

