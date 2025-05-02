from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    ACCESS_TOKEN: str
    OPENAI_API_KEY: str

settings = Settings()
