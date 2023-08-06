from datetime import datetime

from mongoengine.queryset.visitor import Q

from ..models.PullRequestJob import PullRequestJob
from ..schemas import pull_request_job as PullRequestJobSchema


def get_Merge_Request_job(component, buildNum):
    return PullRequestJob.objects(component=component, number=buildNum).first()


def add_Merge_Request_job(data: PullRequestJobSchema.PullRequestJob):
    dateNow = datetime.now()
    data.updateTime = dateNow
    pullRequestJob = PullRequestJob(**data.dict())
    pullRequestJob.save()
    return pullRequestJob


def get_Merge_Request_job_list(query: PullRequestJobSchema.QueryPullRequestJob):
    q = Q()
    if query.component:
        q &= Q(component=query.component)
    if query.startTime:
        q &= Q(updateTime__gte=query.startTime)
    if query.endTime:
        q &= Q(updateTime__lt=query.endTime)
    return {PullRequestJob.objects(q).order_by("-updateTime")}
