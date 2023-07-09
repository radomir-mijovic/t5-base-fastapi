from pydantic import BaseSettings


class Settings(BaseSettings):
    TRANSLATE_PREFIX: str = "/api/v1"
    DOCS_PREFIX: str = "/docs"
