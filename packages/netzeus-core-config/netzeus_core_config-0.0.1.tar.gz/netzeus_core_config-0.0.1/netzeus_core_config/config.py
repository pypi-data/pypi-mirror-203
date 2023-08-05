from pydantic import BaseSettings, PostgresDsn


class AsyncPostgresDsn(PostgresDsn):
    allowed_schemes = {"postgresql+asyncpg"}


class Settings(BaseSettings):
    # App settings
    APP_NAME: str = "NetZeus Core"
    API_BASE_URL: str = "/api/v1"
    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = "admin"

    # Database Settings
    DATABASE_URI: AsyncPostgresDsn = (
        "postgresql+asyncpg://postgres:netzeus@localhost:5432/netzeus"
    )
    DATABASE: str = "netzeus"

    # Security and Authentication Settings
    API_AUTH_URL: str = "/auth/token"
    API_KEY_HEADER: str = "NetZeus-API-Key"
    SECRET_KEY: str = "change-this-secret-key"
    ACCESS_TOKEN_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRES_IN: int = 60 * 60 * 6  # 6 Hours

    class Config:
        env_file = "~/.netzeus_env"
