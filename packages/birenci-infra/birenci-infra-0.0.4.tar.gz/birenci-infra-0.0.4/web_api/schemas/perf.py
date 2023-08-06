from datetime import datetime

from pydantic import BaseModel


class PerfResult(BaseModel):
    jobName: str
    buildID: str
    buildNum: str
    buildURL: str
    model: str
    modelType: str
    modelAccuracy: str = None
    modelPerformance: str = None
    modelMeanLatency: str = None
    startTime: datetime = None
    updateTime: datetime = None


class QueryPerf(BaseModel):
    page: int = 1
    size: int = 10
