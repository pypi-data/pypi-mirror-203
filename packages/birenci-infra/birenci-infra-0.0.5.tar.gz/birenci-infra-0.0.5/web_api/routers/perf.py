from flask import Blueprint, request

from ..handles import build as JenkinsHandle
from ..schemas import jenkins as JenkinsSchema
from ..utils import resp

router = Blueprint("perf", __name__, url_prefix="/api/perf")


@router.route("/", methods=["get"])
def perf_list():
    query = JenkinsSchema.QueryBuildResult(**dict(request.args))
    out = JenkinsHandle.build_list(query)
    return resp.listResp(data=out)


@router.route("/", methods=["post"])
def add_perf():
    data = request.get_json()
    bBuild = JenkinsSchema.BuildResult(**data)
    bBuild.buildLabel = ["perf"]
    out = JenkinsHandle.add_build(bBuild)
    return resp.dictResp(data=out)


@router.route("/", methods=["patch"])
def patch_perf():
    data = request.get_json()
    bBuild = JenkinsSchema.BuildResult(**data)
    out = JenkinsHandle.patch_build(bBuild)
    return resp.dictResp(data=out)
