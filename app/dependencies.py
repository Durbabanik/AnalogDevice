#This code snippet is used to create a dependency function for obtaining a database session in a FastAPI application. 
#It leverages SQLModel to manage database interactions.

from sqlmodel import Session
from app.database import engine

def get_session():
    with Session(engine) as session:
        yield session

