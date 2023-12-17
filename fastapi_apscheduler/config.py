import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    job_store_url: str = os.getenv("SCHEDULER_STORE_URL", "sqlite:///jobs1.sqlite")


settings = Settings()
