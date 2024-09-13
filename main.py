import uvicorn
from fastapi import FastAPI
from app.routes.routes import router
from app.database import Base, engine
from app.middleware.middleware import AuthMiddleware

def create_app():
    app = FastAPI()
    app.add_middleware(AuthMiddleware)
    app.include_router(router)
    return app

app = create_app()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) # running the app
