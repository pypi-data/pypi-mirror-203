from datetime import datetime

from pydantic import BaseModel


class Component(BaseModel):
    name: str
    parentComponent: str
    updatedTime: datetime = None


class QueryComponent(BaseModel):
    name: str = None
    parentComponent: str = None
