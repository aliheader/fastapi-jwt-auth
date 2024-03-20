import os
import secrets
from dotenv import load_dotenv
from sqlalchemy.engine import url

load_dotenv()


class Settings:
    PROJECT_NAME = "JWT Auth Middleware"

    PREFIX: str = "/api"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1

    DB_DRIVER = os.environ.get("DB_DRIVER", "postgresql+psycopg2")
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", "5432")
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_NAME = os.environ.get("DB_NAME")

    DB_URL = url.URL.create(
        DB_DRIVER,
        host=DB_HOST,
        port=DB_PORT,
        username=DB_USER,
        password=DB_PASS.replace("%", "%%"),
        database=DB_NAME,
    )


settings = Settings()
