from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from dotenv import load_dotenv
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
                        raise HTTPException(status_code=401, detail="Invalid credentials")
                

            except Exception:
                raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        else:
            raise HTTPException(status_code=401, detail="Missing Authorization header")

        response = await call_next(request)
        return response
