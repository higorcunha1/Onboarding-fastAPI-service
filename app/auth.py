from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

# Getting the credentials from the environment variables
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

security = HTTPBasic()

# Setting the password hashing 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)): 
    # Directly verifying the credentials
    if credentials.username != username or credentials.password != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username