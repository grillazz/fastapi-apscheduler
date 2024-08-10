from enum import Enum
from pydantic import BaseModel, ConfigDict, Field

config = ConfigDict(
    json_schema_extra={
        "example": {"func": "example.main:pytest_job", "trigger": "interval", "seconds": 3, "id": "pytest_job"}
    }
)


class TriggerEnum(str, Enum):
    interval = "interval"
    cron = "cron"


class Job(BaseModel):
    model_config = config
    func: str = Field()  # TODO: PyObject https://github.com/pydantic/pydantic/issues/4079
    trigger: TriggerEnum = Field(title="Trigger type")
    seconds: int = Field(title="Interval in seconds")
    id: str = Field(title="Job ID")

# TODO: Add this to the Job model to warrant unique IDs
# from pydantic import Field
# from uuid import uuid4
#
# class Job(BaseModel):
#     id: str = Field(default_factory=lambda: str(uuid4()), title="Job ID")
#     # other fields...