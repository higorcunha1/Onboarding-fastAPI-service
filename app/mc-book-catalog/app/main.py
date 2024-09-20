from fastapi import FastAPI
from routes.catalog_routes import router as catalog_router

app = FastAPI()

app.include_router(catalog_router)
