from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class PullRequest(BaseModel):
    pullRequestName: str
    component: str
    pullRequestNumber: str
    pullLink: str = None
    sourceBranch: str = None
    targetBranch: str = None
    commit: str = None
    status: str = None
    prCreatedTime: datetime = None
    prCreatedBy: str = None
    prUpdatedTime: datetime = None
    prUpdatedBy: str = None
    prEndedTime: datetime = None
    prEndedBy: str = None
    updatedTime: datetime = None
    prStatusChecked: bool = False


class UpdatePullRequest(BaseModel):
    status: str = None
    pullLink: str = None
    updatedTime: datetime = None


class QueryPullRequest(BaseModel):
    component: str = None
    components: list = None
    startTime: datetime = None
    endTime: datetime = None


class BarGraphData(BaseModel):
    xAxis = []
    data = []


class ResultData(BaseModel):
    name: str = Optional[str]
    data = []


class PRTableData(BaseModel):
    columns = []
    data = []


class ColumnData(BaseModel):
    title: str = Optional[str]
    dataIndex: str = Optional[str]
    key: str = Optional[str]


class PRRowData(BaseModel):
    key: int = Optional[int]
    name: str = Optional[str]
    pullRequestNumber: str = Optional[str]
    total: int = 0
    passed: int = 0
    failed: int = 0
    unstable: int = 0
    abort: int = 0
    failrate: str = Optional[str]
    reopenTimes: int = 0


class PRColumnName(Enum):
    name = "pr名称"
    pullRequestNumber = "pr number"
    total = "总数"
    passed = "成功"
    failed = "失败"
    unstable = "不稳定"
    abort = "中止"
    failrate = "失败率"
    reopenTimes = "重启次数"


class UserMergRate(BaseModel):
    user: str = Optional[str]
    mergedPR: int = 0
    totalPRJOb: int = 0
    passRate: str = Optional[str]
    passRateFloat: float = Optional[float]


class UserFailRate(BaseModel):
    user: str = Optional[str]
    failedPR: int = 0
    totalPRJOb: int = 0
    failedRate: str = Optional[str]
    failedRateFloat: float = Optional[float]


class UserRowData(BaseModel):
    key: int = Optional[int]
    ranking: int = Optional[int]
    name: str = Optional[str]
    total: int = 0
    merged: int = 0
    passrate: str = "NA"
    failed: int = 0
    failedrate: str = "NA"


class PullRequestRowData(BaseModel):
    key: int = Optional[int]
    ranking: int = Optional[int]
    name: str = Optional[str]
    total: int = 0
    failed: int = 0
    failedrate: str = "NA"
    failedrateFloat: float = Optional[float]
    prURL: str = None


class UserColumnName(Enum):
    ranking = "排名"
    name = "用户名"
    total = "总数"
    merged = "合并"
    passrate = "通过率"
    failed = "失败"
    failedrate = "失败率"


class PullRequestColumnName(Enum):
    ranking = "排名"
    name = "pr名称"
    total = "总数"
    failed = "失败"
    failedrate = "失败率"
    prURL = "pr URL"
