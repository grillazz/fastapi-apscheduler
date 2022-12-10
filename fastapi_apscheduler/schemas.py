from enum import Enum
from pydantic import BaseModel, Field


class TriggerEnum(str, Enum):
    interval = "interval"
    cron = "cron"


class Job(BaseModel):
    func: str = Field()  # TODO: PyObject https://github.com/pydantic/pydantic/issues/4079
    trigger: TriggerEnum = Field(..., title="Trigger type")
    seconds: int = Field(..., title="Interval in seconds")
    id: str = Field(..., title="Job ID")

    class Config:

        schema_extra = {
            "example": {
                "func": "example:main:pytest_job",
                "trigger": "interval",
                "seconds": 3,
                "id": "pytest_job"
            }
        }

