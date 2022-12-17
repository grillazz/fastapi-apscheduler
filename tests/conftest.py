from typing import AsyncGenerator

import httpx
import pytest_asyncio
from httpx import AsyncClient
import pytest
from fastapi import FastAPI

from fastapi_apscheduler.scheduler import add_scheduler
from fastapi_apscheduler.routers import get_jobs_router


@pytest.fixture
def app_factory():
    def _app_factory() -> FastAPI:
        app = FastAPI()
        add_scheduler(app, "sqlite:///jobs.sqlite")
        app.include_router(get_jobs_router(), prefix="/scheduler", tags=["scheduler"])
        return app

    return _app_factory


@pytest.fixture
def get_test_client():
    async def _get_test_client(app: FastAPI) -> AsyncGenerator[httpx.AsyncClient, None]:
        async with AsyncClient(
            app=app,
            base_url="http://fiveoclock/v1",
        ) as test_client:
            yield test_client

    return _get_test_client


@pytest_asyncio.fixture
async def test_app_client(app_factory) -> AsyncGenerator[AsyncClient, None]:
    app = app_factory()
    yield get_test_client(app)
