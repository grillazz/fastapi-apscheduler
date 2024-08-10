import os

from pydantic_settings import BaseSettings


# TODO: introduce env varialble to better customie job store url

class Settings(BaseSettings):
    job_store_url: str = os.getenv("SCHEDULER_STORE_URL", "sqlite:///jobs1.sqlite")


settings = Settings()
