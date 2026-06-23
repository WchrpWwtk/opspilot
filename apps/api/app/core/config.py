from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_ENV: str = "local"
    DATABASE_URL: str = (
        "postgresql+asyncpg://opspilot:change_me_for_local_dev@postgres:5432/opspilot"
    )
    CORS_ALLOWED_ORIGINS: str = "http://localhost:3000"

    model_config = SettingsConfigDict(extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
