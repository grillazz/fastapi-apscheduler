from collections.abc import AsyncGenerator

from asgi_lifespan import LifespanManager
import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from fastapi_apscheduler.scheduler import lifespan as add_scheduler
from fastapi_apscheduler.routers import get_jobs_router


@pytest.fixture(
    scope="session",
    params=[
        pytest.param(("asyncio", {"use_uvloop": False}), id="asyncio"),
        pytest.param(("asyncio", {"use_uvloop": True}), id="asyncio+uvloop"),
    ],
)
def anyio_backend(request):
    return request.param


@pytest.fixture
def app_factory():
    def _app_factory() -> FastAPI:
        app = FastAPI(lifespan=add_scheduler)

        app.include_router(get_jobs_router(), prefix="/scheduler", tags=["scheduler"])
        return app

    return _app_factory


@pytest.fixture
def get_test_client():
    async def _get_test_client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
        async with LifespanManager(app):
            async with AsyncClient(
                app=app,
                base_url="http://fiveoclock",
            ) as test_client:
                yield test_client

    return _get_test_client


@pytest.fixture
async def test_app_client(get_test_client, app_factory) -> AsyncGenerator[AsyncClient, None]:
    app = app_factory()
    async for client in get_test_client(app):
        yield client


#
# import pytest
# from httpx import AsyncClient, ASGITransport
#
# from app.database import engine
# from app.main import app
# from app.models.base import Base
# from app.redis import get_redis


#
# @pytest.fixture(scope="session")
# async def start_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#     # for AsyncEngine created in function scope, close and
#     # clean-up pooled connections
#     await engine.dispose()
#
#
# @pytest.fixture(scope="session")
# async def client(start_db) -> AsyncClient:
#
#     transport = ASGITransport(
#         app=app,
#     )
#     async with AsyncClient(
#         # app=app,
#         base_url="http://testserver/v1",
#         headers={"Content-Type": "application/json"},
#         transport=transport,
#     ) as test_client:
#         app.redis = await get_redis()
#         yield test_client
