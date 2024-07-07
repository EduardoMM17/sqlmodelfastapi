import os
from pydantic_settings import BaseSettings, SettingsConfigDict

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))
database_url = f"sqlite+aiosqlite:///{os.path.join(base_dir, sqlite_file_name)}"


class Settings(BaseSettings):

    # to tell settings to read from .env
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    SQLITE_URL: str = database_url


settings = Settings()
