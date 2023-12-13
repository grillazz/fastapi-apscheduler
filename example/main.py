from fastapi import FastAPI

from fastapi_apscheduler.utils import get_logger
from fastapi_apscheduler.routers import get_jobs_router
from fastapi_apscheduler.scheduler import lifespan

logger = get_logger(__name__)

app = FastAPI(lifespan=lifespan)

app.include_router(get_jobs_router(), prefix="/scheduler", tags=["scheduler"])


async def pytest_job():
    logger.info("test_job")

# TODO: job to test netowrk seed with ookla pytjhon client via apscheduler
# TODO: mount via lifespan should happen as meny time as many workers you add
# TODO: fix duppl;icates via redis aio locks
