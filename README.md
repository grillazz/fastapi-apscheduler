# fastapi-apscheduler


[![Build Status](https://travis-ci.com/viniciuschiele/fastapi-apscheduler.svg?branch=main)](https://travis-ci.com/viniciuschiele/fastapi-apscheduler)
[![PyPI version](https://badge.fury.io/py/fastapi-apscheduler.svg)](https://badge.fury.io/py/fastapi-apscheduler)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

```bash
pip install fastapi-apscheduler
```

## Usage

```python
from fastapi import FastAPI

from fastapi_apscheduler.utils import get_logger
from fastapi_apscheduler.routers import get_jobs_router
from fastapi_apscheduler.scheduler import lifespan

logger = get_logger(__name__)

app = FastAPI(lifespan=lifespan)

app.include_router(get_jobs_router(), prefix="/scheduler", tags=["scheduler"])


async def pytest_job():
    logger.info("test_job")
```



## Build and publish to pypi with poetry
```bash
poetry build

Building fastapi-apscheduler (0.0.x)
  - Building sdist
  - Built fastapi_apscheduler-0.0.x.tar.gz
  - Building wheel
  - Built fastapi_apscheduler-0.0.x-py3-none-any.whl


poetry config pypi-token.pypi <token>


poetry publish

Publishing fastapi-apscheduler (0.0.6) to PyPI
 - Uploading fastapi_apscheduler-0.0.6-py3-none-any.whl 100%
 - Uploading fastapi_apscheduler-0.0.6.tar.gz 100%
```

## Run local instance of worker with uvicorn
```bash
uvicorn example.main:app --workers 1 --port 8084 --log-level debug --env-file example/.env
```

## TODO:
- add CI
- add tests to CI
- add coverage to CI