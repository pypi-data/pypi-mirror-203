from flask import Blueprint, request

from ..handles import build as JenkinsHandle
from ..schemas import jenkins as JenkinsSchema
from ..utils import resp

router = Blueprint("build", __name__, url_prefix="/api/build")


@router.route("/", methods=["get"])
def build_list():
    query = JenkinsSchema.QueryBuildResult(**dict(request.args))
    out = JenkinsHandle.build_list(query)
    return resp.listResp(data=out)


@router.route("/", methods=["post"])
def add_build():
    data = request.get_json()
    bBuild = JenkinsSchema.BuildResult(**data)
    out = JenkinsHandle.add_build(bBuild)
    if out:
        return resp.dictResp(data=out)
    else:
        return resp.errResp(**resp.ERROR_202)


@router.route("/", methods=["put"])
def put_build():
    data = request.get_json()
    bBuild = JenkinsSchema.BuildResult(**data)
    out = JenkinsHandle.update_build(bBuild)
    return resp.dictResp(data=out)


@router.route("/", methods=["patch"])
def patch_build():
    data = request.get_json()
    bBuild = JenkinsSchema.BuildResult(**data)
    out = JenkinsHandle.patch_build(bBuild)
    return resp.dictResp(data=out)
