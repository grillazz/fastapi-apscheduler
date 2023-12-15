from contextlib import asynccontextmanager

from fastapi import FastAPI
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .utils import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    jobstores = {"default": SQLAlchemyJobStore(url="sqlite:///jobs1.sqlite")}
    app.state.scheduler = AsyncIOScheduler(jobstores=jobstores)
    try:
        app.state.scheduler.start()
        yield
    finally:
        app.state.scheduler.shutdown()
