import asyncio

from fastapi import FastAPI

from fastapi_apscheduler.utils import get_logger
from fastapi_apscheduler.routers import get_jobs_router
from fastapi_apscheduler.scheduler import lifespan

logger = get_logger(__name__)

app = FastAPI(lifespan=lifespan)

app.include_router(get_jobs_router(), prefix="/scheduler", tags=["scheduler"])


async def pytest_job():
    logger.info("dupa_test_job")


# TODO: job to test netowrk seed with ookla python client via apscheduler
# TODO: mount via lifespan should happen as meny time as many workers you add
# TODO: fix duppl;icates via redis aio locks


# TODO: test with gunicorn uvicorn workers
# TODO: gunicorn example.main:app -w 5 -k uvicorn.workers.UvicornWorker
# TODO: add some gui for example with i.e. https://github.com/pydantic/FastUI
