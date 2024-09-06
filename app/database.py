from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:admin@postgres/mydatabase")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# managing the database session class 
class DatabaseSession:
    def __init__(self):
        # Initializes the database session
        self.db = SessionLocal()

    def __enter__(self):
        # Method that returns the database session
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Method that commits the changes in the database
        try:
            if exc_type is None:
                # If there is no exception, commit the changes
                self.db.commit()
            else:
                # If there is an exception, rollback the changes
                self.db.rollback()
        finally:
            # Always close the session
            self.db.close()

    def commit(self):
        # Commit the changes into the db.
        try:
            self.db.commit()
        except:
            self.db.rollback()
            raise

    def close(self):
        # Close the db session.
        self.db.close()

    def add(self, instance):
        # Adds an instance into the session.
        self.db.add(instance)

    def refresh(self, instance):
        # Updates the instance in the session.
        self.db.refresh(instance)

    def delete(self, instance):
        # Removes the instance from the session.
        self.db.delete(instance)