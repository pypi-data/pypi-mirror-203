from mongoengine import (
    BooleanField,
    DateTimeField,
    DictField,
    FloatField,
    ListField,
    StringField,
)

from ..mongo import mongo as db


class Job(db.Document):
    jobName = StringField(required=True)
    jobBaseName = StringField()
    desc = StringField()
    startTime = DateTimeField()
    updateTime = DateTimeField()

    meta = {"strict": False}


class JobBuildResult(db.Document):
    jobName = StringField()
    jobBaseName = StringField()
    buildNum = StringField()
    buildID = StringField()
    buildURL = StringField()
    jenkinsURL = StringField()
    gitBranch = StringField()
    gitCommit = StringField()
    status = StringField()
    duration = StringField()
    buildLabel = ListField()
    result = DictField()
    extraInfo = DictField()
    startTime = DateTimeField()
    updateTime = DateTimeField()

    meta = {"strict": False}


class PerfResult(db.Document):
    jobName = StringField()
    buildID = StringField()
    buildURL = StringField()
    model = StringField()
    modelType = StringField()
    modelAccuracy = FloatField()
    modelPerformance = FloatField()
    modelMeanLatency = FloatField()
    startTime = DateTimeField()
    updateTime = DateTimeField()

    meta = {"strict": False}
