from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    MONGODB_URI: str

settings = Settings()