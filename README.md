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
from fastapi_apscheduler.scheduler import add_scheduler
from fastapi_apscheduler.routers import get_jobs_router

logger = get_logger(__name__)

app = FastAPI()


add_scheduler(app, "sqlite:///jobs.sqlite")

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

poetry publish

Publishing fastapi-apscheduler (0.0.x) to PyPI
 - Uploading fastapi_apscheduler-0.0.x-py3-none-any.whl 100%
```

## TODO:
- add CI
- add tests to CI
- add coverage to CI