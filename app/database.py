#set up a connection to the database using SQLModel and the 
#configuration settings provided in your FastAPI application.

from sqlmodel import create_engine
from app.config import settings

engine = create_engine(settings.database_url)

