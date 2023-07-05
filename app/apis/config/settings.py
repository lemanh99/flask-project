import os
from typing import List

from pydantic import BaseSettings, Field


class CORSSettings(BaseSettings):
    FRONTEND_URL: str = Field(default="http://localhost:3000")
    DEBUG_FRONT_URLS: List[str] = []


class JWTAuthenticationSettings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    ALGORITHM: str = "HS256"
    JWT_SECRET_KEY: str = ""
    JWT_REFRESH_SECRET_KEY: str = ""


class DatabaseSettings(BaseSettings):
    DB_ENGINE: str = "mysql+pymysql"
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str


class Settings(
    CORSSettings,
    DatabaseSettings
):
    class Config:
        env_file = "app/.env"


settings = Settings()
