from datetime import datetime

from mongoengine.queryset.visitor import Q

from ..models.PullRequest import PullRequest
from ..schemas import pull_request as PullRequestSchema


# 添加pr数据
def add_Merge_Request(data: PullRequestSchema.PullRequest):
    dateNow = datetime.now()
    data.updatedTime = dateNow
    data.prStatusChecked = False
    pullRequest = PullRequest(**data.dict())
    pullRequest.save()
    return pullRequest


# 更新pr数据
def update_pull_reqauest(data: PullRequestSchema.UpdatePullRequest):
    pr = get_Merge_Request(data.pullLink)
    pr.update(status=data.status, updatedTime=datetime.now())
    pr.reload
    return pr


# 根据条件获取pr
def get_Merge_Request(pullLink):
    return PullRequest.objects(pullLink=pullLink).first()


def get_Merge_Request_list(query: PullRequestSchema.QueryPullRequest):
    q = Q()
    if query.component:
        q &= Q(component=query.component)
    if query.startTime:
        q &= Q(prCreatedTime__gte=query.startTime)
    if query.endTime:
        q &= Q(prCreatedTime__lt=query.endTime)
    return {PullRequest.objects(q).order_by("-prCreatedTime")}


def get_Merge_Request_list_and_job_list(query: PullRequestSchema.QueryPullRequest):
    q = Q()
    if query.component:
        q &= Q(component=query.component)
    if query.components:
        q &= Q(component__in=query.components)
    if query.startTime:
        q &= Q(prCreatedTime__gte=query.startTime)
    if query.endTime:
        q &= Q(prCreatedTime__lt=query.endTime)
    pipeline = [
        {
            "$lookup": {
                "from": "Merge_Request_job",  # 要一起合并的数据库
                "localField": "pullLink",  # Merge_Request中的字段
                "foreignField": "pullLink",  # Merge_Request_job中的字段
                "as": "jobList",  # 将查询到的表合并成一个list
            }
        }
    ]
    result = PullRequest.objects(q).aggregate(*pipeline)
    return result
