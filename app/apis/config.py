from typing import List

from pydantic import BaseSettings, Field


class CORSSettings(BaseSettings):
    FRONTEND_URL: str = Field(default="http://localhost:3000")
    DEBUG_FRONT_URLS: List[str] = []


class Settings(
    CORSSettings,
):
    class Config:
        env_file = ".env"


settings = Settings()
