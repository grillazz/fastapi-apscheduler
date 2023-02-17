from fastapi import FastAPI
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .utils import get_logger

logger = get_logger(__name__)


class AsyncScheduler(AsyncIOScheduler):
    def __init__(self, url=None):
        self.jobstores = {"default": SQLAlchemyJobStore(url=url)}
        super().__init__(jobstores=self.jobstores)


def add_scheduler(app: FastAPI, url: str) -> FastAPI:
    @app.on_event("startup")
    def start_scheduler() -> None:
        app.state.scheduler = AsyncScheduler(url)
        app.state.scheduler.start()
        logger.info(f"startup event - {app.state.scheduler.state=}")

    @app.on_event("shutdown")
    def stop_scheduler() -> None:
        app.state.scheduler.shutdown()

    return app
