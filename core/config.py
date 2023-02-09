import secrets
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
import logging
from os import getenv


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = getenv("SECRET")
    PROJECT_NAME: str = "Inventory Events"
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = ["http://localhost", "http://localhost:4200", "http://localhost:3000", "http://localhost:8080", "https://localhost", "https://localhost:4200", "https://localhost:3000","https://localhost:8080", "http://dev.{{cookiecutter.domain_main}}", "https://{{cookiecutter.domain_staging}}", "https://{{cookiecutter.domain_main}}", "http://local.dockertoolbox.tiangolo.com", "http://localhost.tiangolo.com"]
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    class Config:
        case_sensitive = True


settings = Settings()