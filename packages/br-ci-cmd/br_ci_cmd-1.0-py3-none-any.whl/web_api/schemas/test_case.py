from datetime import datetime

from pydantic import BaseModel


class TestCase(BaseModel):
    name: str = None
    status: str = None
    result: str = None
    reason: str = None
    type: str = None
    startTime: datetime = None
    endTime: datetime = None
    duration: int = None
    jobName: str = None
    jobBuildNum: int = None
    jobIsDeug: bool = False
    updatedTime: datetime = None
