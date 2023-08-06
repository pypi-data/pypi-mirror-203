from typing import List

from mongoengine import BooleanField, DateTimeField, DictField, ListField, StringField

from ..mongo import mongo as db


class PullRequestJob(db.Document):
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
    startTime = DateTimeField()
    endTime = DateTimeField()
    updateTime = DateTimeField()
    isDebug = BooleanField()
    component = StringField()
    pullLink = StringField()
