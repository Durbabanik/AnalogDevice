#This setup is particularly useful in different environments (development, testing, production) where you can easily switch 
#configurations by changing environment variables or the .env file.
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()

