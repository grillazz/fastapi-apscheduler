import asyncio

from fastapi import FastAPI

from fastapi_apscheduler.utils import get_logger
from fastapi_apscheduler.routers import get_jobs_router
from fastapi_apscheduler.scheduler import lifespan

import redis.asyncio as redis

logger = get_logger(__name__)

app = FastAPI(lifespan=lifespan)

app.include_router(get_jobs_router(), prefix="/scheduler", tags=["scheduler"])


async def get_redis():
    return await redis.from_url(
        "redis://localhost:6379/2",
        encoding="utf-8",
        decode_responses=True,
    )

async def pytest_job():
    logger.info("dupa_test_job")

# async def pytest_job():
#     logger.info("dupa_test_job")



