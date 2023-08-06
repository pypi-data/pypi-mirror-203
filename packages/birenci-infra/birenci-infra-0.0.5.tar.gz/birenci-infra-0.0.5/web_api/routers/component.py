from typing import Set

from flask import Blueprint, request

from ..handles import component as ComponentHandle
from ..schemas import component as ComponentSchemas
from ..utils import resp

router = Blueprint("component", __name__, url_prefix="/api/component")


# 新增component
@router.route("/add-list", methods=["post"])
def add_component_list():
    data = request.get_json()
    list = data["data"]
    result = []
    for component in list:
        component = ComponentSchemas.Component(**component)
        result.append(ComponentHandle.add_component(component))
    return resp.dictResp(data=result)


# 父级component列表
@router.route("/parent-list", methods=["get"])
def parent_component_list():
    result = ComponentHandle.get_components()
    parent_component_list = []
    for component_list in result:
        for component in component_list:
            if component.parentComponent not in parent_component_list:
                parent_component_list.append(component.parentComponent)

    return resp.dictResp(data=parent_component_list)


# 根据parent component 获取component列表
@router.route("/list", methods=["get"])
def component_list():
    parent_component = request.args.get("parentComponent")
    query = ComponentSchemas.QueryComponent()
    query.parentComponent = parent_component
    result = ComponentHandle.get_component_list_by_parent(query)
    list = []
    for component_list in result:
        for component in component_list:
            if component.name not in component_list:
                list.append(component.name)

    return resp.dictResp(data=list)
