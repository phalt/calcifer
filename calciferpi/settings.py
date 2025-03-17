import platform

from pydantic_settings import BaseSettings

VERSION = "0.1.0"


def split_ver():
    return [int(v) for v in platform.python_version().split(".")]


class Settings(BaseSettings):
    DATA_PIN: int = 4
    SERVER_DEBUG: bool = False
    SERVER_PORT: int = 80
    DEBUG: bool = False

    class Config:
        env_file = "~/.config/calciferpi"
        env_file_encoding = "utf-8"


settings = Settings()

PY_VERSION = split_ver()
