from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, field_validator


class Settings(BaseSettings):
    PROJECT_NAME: str

    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_URI: Optional[str] = None

    # @field_validator("POSTGRES_URI")
    # def validate_postgres_conn(cls, v: Optional[str], values: Dict[str, Any]) -> str:
    #     if isinstance(v, str):
    #         return v
    #     password: SecretStr = values.get("POSTGRES_PASSWORD", SecretStr(""))
    #     return "{scheme}://{user}:{password}@{host}/{db}".format(
    #         scheme="postgresql+asyncpg",
    #         user=values.get("POSTGRES_USER"),
    #         password=password.get_secret_value(),
    #         host=values.get("POSTGRES_HOST"),
    #         db=values.get("POSTGRES_DB"),
    #     )

    RABBITMQ_HOST: str

    REDIS_HOST: str
    REDIS_PORT: int
    
    model_config = SettingsConfigDict(env_file=".env")
    

setting = Settings()