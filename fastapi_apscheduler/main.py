from fastapi import FastAPI

from .utils import get_logger
from .scheduler import add_scheduler
from .routers import get_users_router

logger = get_logger(__name__)

app = FastAPI()

add_scheduler(app, "sqlite:///jobs.sqlite")

app.include_router(
   get_users_router(), prefix="/scheduler", tags=["scheduler"]
)


async def pytest_job():
    logger.info("test_job")
