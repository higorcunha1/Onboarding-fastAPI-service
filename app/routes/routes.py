from fastapi import APIRouter
from pydantic import BaseModel
from app.controller.controller import hello_response, echo_response

router = APIRouter()

@router.get("/hello") # hello world route (GET)
async def hello_world():
    return hello_response()

class EchoRequest(BaseModel): # data model for the POST request
    value: str

@router.post("/echo") # Echo route (POST)
async def echo(request: EchoRequest):
    return echo_response(request.value)