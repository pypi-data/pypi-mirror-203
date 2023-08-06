from datetime import datetime

from mongoengine.queryset.visitor import Q

from ..models.JenkinsResult import Job, JobBuildResult
from ..schemas import jenkins as JenkinsSchema
from ..utils import dict_utils


def job_list():
    return Job.objects()


def get_build(buildURL, buildID):
    return JobBuildResult.objects(buildURL=buildURL, buildID=buildID).first()


def build_list(query: JenkinsSchema.QueryBuildResult):
    q = Q()
    if query.buildID:
        q &= Q(buildID=query.buildID)
    if query.buildURL:
        q &= Q(buildURL=query.buildURL)
    if query.jobName:
        q &= Q(jobName=query.jobName)
    if query.buildNum:
        q &= Q(buildNum=query.buildNum)
    if query.status:
        q &= Q(status=query.status)
    return {
        "totals": JobBuildResult.objects(q).count(),
        "page": query.page,
        "size": query.size,
        "data": (
            JobBuildResult.objects(q)
            .order_by("-startTime")
            .skip((query.page - 1) * query.size)
            .limit(query.size)
        ),
    }


def add_build(data: JenkinsSchema.BuildResult):
    mBuild = get_build(data.buildURL, data.buildID)
    if mBuild:
        return {}
    dateNow = datetime.now()
    data.startTime = dateNow
    data.updateTime = dateNow
    jobBuildResult = JobBuildResult(**data.dict())
    jobBuildResult.save()
    return jobBuildResult


def update_build(data: JenkinsSchema.BuildResult):
    mBuild = get_build(data.buildURL, data.buildID)
    if data.result:
        result = dict_utils.merge(mBuild.result, data.result)
    else:
        result = mBuild.result
    mBuild.update(status=data.status, result=result, updateTime=datetime.now())
    mBuild.reload()
    return mBuild


def patch_build(data: JenkinsSchema.BuildResult):
    mBuild = get_build(data.buildURL, data.buildID)
    if mBuild:
        if data.result:
            result = dict_utils.merge(mBuild.result, data.result)
        else:
            result = mBuild.result
        mBuild.update(status=data.status, result=result, updateTime=datetime.now())
        mBuild.reload()
    else:
        mBuild = add_build(data)
    return mBuild
