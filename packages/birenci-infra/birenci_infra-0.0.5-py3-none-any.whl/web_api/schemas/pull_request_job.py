from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel

from . import jenkins


class PullRequestJob(jenkins.BuildResult):
    buildID: str = None
    isDebug: bool = False
    component: str = None
    pullLink: str = None
    endTime: datetime = None


class QueryPullRequestJob(BaseModel):
    component: str = None
    startTime: datetime = None
    endTime: datetime = None


class JobTableData(BaseModel):
    columns = []
    data = []


class ColumnData(BaseModel):
    title: str = Optional[str]
    dataIndex: str = Optional[str]
    key: str = Optional[str]


class JobRowData(BaseModel):
    key: str = Optional[str]
    component: str = Optional[str]
    total: int = 0
    passed: int = 0
    failed: int = 0
    unstable: int = 0
    abort: int = 0
    failrate: str = Optional[str]


class JobColumnName(Enum):
    component = "组件"
    total = "总数"
    passed = "成功"
    failed = "失败"
    unstable = "不稳定"
    abort = "中止"
    failrate = "失败率"
