from fastapi_apscheduler.utils import get_logger

logger = get_logger(__name__)


async def pytest_job():
    logger.info("test_job")
