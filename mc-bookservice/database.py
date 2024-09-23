from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:admin@postgres/mydatabase")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
