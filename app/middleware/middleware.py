from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
import base64
import os

# Loading the environment variables
load_dotenv()

# Defining the password 
PASSWORD = os.getenv("PASSWORD")

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Verify if the request has the Authorization header
        auth = request.headers.get('Authorization')
        if auth:
            try:
                # Decodificar credenciais básicas (Basic Auth)
                scheme, credentials = auth.split()
                if scheme.lower() == "basic":
                    decoded = base64.b64decode(credentials).decode('utf-8')
                    username, password = decoded.split(':')

                    # Checking if the password is correct
                    if password != PASSWORD:
                        return JSONResponse(
                            status_code=401,
                            content={"detail": "Invalid credentials"}
                        )


            except Exception:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Invalid authentication credentials"}
                )
        else:
            return JSONResponse(
                status_code=401,
                content={"detail": "Missing Authorization header"}
            )

        response = await call_next(request)
        return response
