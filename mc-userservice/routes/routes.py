from fastapi import APIRouter
from controller.controller import UserController, hello_response, echo_response
from pydantic import BaseModel
router = APIRouter()

# Defining the request models for the routes
class UserRequest(BaseModel):
    name: str

# Echo route
class EchoRequest(BaseModel): 
    value: str


# Routes related to users 
user_controller = UserController()

@router.post("/users/")
# Requiring authentication to the route
def add_user(user: UserRequest):
    return user_controller.create(user.name)

# Hello world route
@router.get("/hello") 
async def hello_world():
    return hello_response()


@router.post("/echo") 
async def echo(request: EchoRequest):
    return echo_response(request.value)
