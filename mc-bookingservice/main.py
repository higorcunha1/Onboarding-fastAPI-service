import uvicorn
from fastapi import FastAPI
from routes.booking_routes import router
from database import Base, engine
from middleware.middleware import AuthMiddleware

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
    uvicorn.run(app, host="0.0.0.0", port=8002, reload=True) # running the app
