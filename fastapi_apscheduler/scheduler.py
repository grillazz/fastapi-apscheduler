from contextlib import asynccontextmanager

from fastapi import FastAPI
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .utils import get_logger
from .config import settings

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    _job_store = {"default": SQLAlchemyJobStore(url=settings.job_store_url)}
    _app.scheduler = AsyncIOScheduler(jobstores=_job_store)
    try:
        _app.scheduler.start()
        logger.info("Scheduler started")
        yield
    finally:
        _app.scheduler.shutdown()
        logger.info("Scheduler shutdown")
