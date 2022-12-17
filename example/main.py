from fastapi import FastAPI

from fastapi_apscheduler.utils import get_logger
from fastapi_apscheduler.scheduler import add_scheduler
from fastapi_apscheduler.routers import get_jobs_router

logger = get_logger(__name__)

app = FastAPI()

add_scheduler(app, "sqlite:///jobs.sqlite")

app.include_router(get_jobs_router(), prefix="/scheduler", tags=["scheduler"])


async def pytest_job():
    logger.info("test_job")
