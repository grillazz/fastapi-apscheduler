from contextlib import asynccontextmanager
import os
from fastapi import FastAPI
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .utils import get_logger

logger = get_logger(__name__)

import redis.asyncio as redis
from pottery import AIORedLock

async def get_redis():
    return await redis.from_url(
        "redis://localhost:6379/2",
        encoding="utf-8",
        decode_responses=True,
    )

async def create_scheduler(app, db_url="sqlite:///jobs1.sqlite"):
    _pid = os.getpid()
    logger.info(f"create_scheduler pid: {_pid}")
    jobstores = {"default": SQLAlchemyJobStore(url=db_url)}
    app.state.scheduler = AsyncIOScheduler(jobstores=jobstores)

    app.state.scheduler.start()


def stop_scheduler(app):
    app.state.scheduler.shutdown()


    # app.state.scheduler.shutdown()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_scheduler(app)
    yield
    stop_scheduler(app)


