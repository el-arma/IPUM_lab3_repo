# settings.py
from pydantic_settings import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @validator("ENVIRONMENT")
    def validate_environment(cls, value):
        allowed = {"dev", "test", "prod"}
        if value not in allowed:
            raise ValueError(
                f"ENVIRONMENT must be one of {allowed}, got '{value}' instead."
            )
        return value
