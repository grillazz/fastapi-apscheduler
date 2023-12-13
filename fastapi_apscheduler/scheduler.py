from contextlib import asynccontextmanager

from fastapi import FastAPI
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .utils import get_logger

logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    jobstores = {"default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")}
    app.state.scheduler = AsyncIOScheduler(jobstores=jobstores)  # TODO: set this as variable via BaseConfig class etc
    app.state.scheduler.start()
    logger.info(f"startup event - {app.state.scheduler.state=}")
    try:
        yield
    finally:
        app.state.scheduler.shutdown()
