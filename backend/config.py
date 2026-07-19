from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent

class Settings(BaseSettings):
    APP_NAME: str = "StadiumMind AI"
    VERSION: str = "2.0.0"
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = True
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    FRONTEND_URL: str = "http://localhost:5173"

    GROQ_API_KEY: str = Field(
        default=""
    )
    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    MAX_INCIDENT_HISTORY: int = 500

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()