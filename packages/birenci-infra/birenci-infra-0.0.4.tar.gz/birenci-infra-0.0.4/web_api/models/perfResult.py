from mongoengine import DateTimeField, FloatField, StringField

from ..mongo import mongo as db


class PerfResult(db.Document):
    buildID = StringField()
    buildURL = StringField()
    status = StringField()
    model = StringField()
    modeltype = StringField()
    accuracy = FloatField()
    performance = FloatField()
    mean_latency = FloatField()
    startTime = DateTimeField()
    updateTime = DateTimeField()

    meta = {"strict": False}
