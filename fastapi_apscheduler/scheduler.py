from contextlib import asynccontextmanager

from fastapi import FastAPI
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .utils import get_logger
from .config import settings

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    jobstores = {"default": SQLAlchemyJobStore(url=settings.job_store_url)}
    app.state.scheduler = AsyncIOScheduler(jobstores=jobstores)
    try:
        app.state.scheduler.start()
        yield
    finally:
        app.state.scheduler.shutdown()
