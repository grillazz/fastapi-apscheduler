from datetime import datetime, timezone

import pytest
from starlette import status
from httpx import AsyncClient


pytestmark = pytest.mark.anyio


def aware_utcnow():
    return str(datetime.now(timezone.utc))


class TestRouters:
    async def test_add_job(self, test_app_client: AsyncClient):
        client = test_app_client
        response = await client.post(
            "/scheduler",
            json={
                "func": "example.main:pytest_job",
                "trigger": "interval",
                "seconds": 666,
                "id": f"pytest_job+{aware_utcnow()}",
            },
        )
        assert response.status_code == status.HTTP_201_CREATED
