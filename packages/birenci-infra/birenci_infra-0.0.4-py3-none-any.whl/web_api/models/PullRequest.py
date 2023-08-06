from typing import List

from mongoengine import BooleanField, DateTimeField, StringField

from ..mongo import mongo as db


class PullRequest(db.Document):
    pullRequestName = StringField()
    component = StringField()
    pullRequestNumber = StringField()
    pullLink = StringField()
    sourceBranch = StringField()
    targetBranch = StringField()
    commit = StringField()
    status = StringField()
    prCreatedTime = DateTimeField()
    prCreatedBy = StringField()
    prUpdatedTime = DateTimeField()
    prUpdatedBy = StringField()
    prEndedTime = DateTimeField()
    prEndedBy = StringField()
    updatedTime = DateTimeField()
    prStatusChecked = BooleanField()
