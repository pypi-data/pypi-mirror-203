from mongoengine import BooleanField, DateTimeField, IntField, StringField

from ..mongo import mongo as db


class TestCase(db.Document):
    name = StringField()
    status = StringField()
    result = StringField()
    reason = StringField()
    type = StringField()
    startTime = DateTimeField()
    endTime = DateTimeField()
    duration = IntField()
    jobName = StringField()
    jobBuildNum = IntField()
    jobIsDeug = BooleanField()
    updatedTime = DateTimeField()
