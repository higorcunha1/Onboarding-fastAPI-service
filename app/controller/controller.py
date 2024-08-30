from fastapi.responses import JSONResponse

def hello_response():
    return JSONResponse(content={"message": "Hello World"})

def echo_response(value: str):
    return JSONResponse(content={"message": f"Received: {value}"})
