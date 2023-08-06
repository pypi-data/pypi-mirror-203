from cgi import test
from datetime import datetime, timedelta
from typing import Set

import pandas as pd
from flask import Blueprint, request

from ..handles import pull_request as PullRequestHandle
from ..handles import test_case as TestCaseHandle
from ..schemas import pull_request as PullRequestSchema
from ..schemas import test_case as TestCaseSchema
from ..utils import resp

router = Blueprint("test_case", __name__, url_prefix="/api/test-case")


# 新增test case
@router.route("/add-file", methods=["post"])
def add_test_case():
    try:
        # 要读取的csv文件
        data = pd.read_csv(request.files["file"])
        # 处理csv文件的数据
        all = data["name"].values.tolist()
        print(data.values.tolist())
        data_list = data.values.tolist()
        result_list = []
        for dt in data_list:
            test_case = TestCaseSchema.TestCase()
            test_case.name = dt[0]
            test_case.status = dt[1]
            test_case.result = dt[2]
            test_case.reason = dt[3]
            test_case.type = dt[4]
            test_case.startTime = dt[5]
            test_case.endTime = dt[6]
            test_case.duration = dt[7]
            test_case.jobName = dt[8]
            test_case.jobBuildNum = dt[9]
            test_case.jobIsDeug = dt[10]
            out = TestCaseHandle.add_test_case(test_case)
            result_list.append(out)

        return resp.dictResp(data=result_list)
    except Exception as e:
        print(e)
        return resp.errResp()


# 失败测试用例top n
@router.route("/most-failed-test-case", methods=["get"])
def get_most_failed_test_case():
    try:
        date = (
            request.args.get("date")
            if request.args.get("date")
            else datetime.now().strftime("%Y-%m-%d")
        )
        day_span = (
            request.args.get("daySpan", 7, type=int)
            if request.args.get("daySpan")
            else 7
        )
        component = request.args.get("component")

        # 查询条件query
        query = PullRequestSchema.QueryPullRequest()
        current_time = datetime.strptime(date, "%Y-%m-%d")
        query.endTime = current_time + timedelta(days=1)
        query.startTime = query.endTime - timedelta(days=day_span)
        if component:
            query.component = component
        # 根据查询条件获取pr list
        result = PullRequestHandle.get_Merge_Request_list_and_test_case_list(query)

    except Exception as e:
        print(e)
        return resp.errResp()
