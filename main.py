import uvicorn
from fastapi import FastAPI
from app.routes.routes import router
from app.database import Base, engine

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) # running the app
