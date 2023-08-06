from datetime import datetime, timedelta
from itertools import groupby

from flask import Blueprint, request

from ..handles import pull_request_job as PullRequestJobHandle
from ..schemas import pull_request_job as PullRequestJobSchema
from ..utils import resp

router = Blueprint("Merge_Request_job", __name__, url_prefix="/api/pr-job")


# 新增pr job
@router.route("/add", methods=["post"])
def add_build():
    data = request.get_json()
    pr = PullRequestJobSchema.PullRequestJob(**data)
    out = PullRequestJobHandle.add_Merge_Request_job(pr)
    return resp.dictResp(data=out)


# pr job列表
@router.route("/list", methods=["get"])
def get_Merge_Request_job_list_with_detail():
    try:
        date = (
            request.args.get("date")
            if request.args.get("date")
            else datetime.now().strftime("%Y-%m-%d")
        )
        day_span = (
            request.args.get("daySpan", 7, int) if request.args.get("daySpan") else 7
        )
        query = PullRequestJobSchema.QueryPullRequestJob()
        query.component = request.args.get("component")
        current_time = datetime.strptime(date, "%Y-%m-%d")
        query.endTime = current_time + timedelta(days=1)
        query.startTime = query.endTime - timedelta(days=day_span)

        # 根据查询条件获取pr list
        result_set = PullRequestJobHandle.get_Merge_Request_job_list(query)
        Merge_Request_job_list = []
        for pr_list in result_set:
            for pr_job in pr_list:
                pr_job.updatedTime = pr_job.updateTime.strftime("%Y-%m-%d")
                Merge_Request_job_list.append(pr_job)

        # 根据component对pr job进行分组
        Merge_Request_job_list = sorted(
            Merge_Request_job_list, key=lambda x: x["component"]
        )
        # 根据component对pr job进行分组
        component_group = groupby(Merge_Request_job_list, key=lambda x: x["component"])

        # 构造返回参数
        table_data = PullRequestJobSchema.JobTableData()
        for column_name in PullRequestJobSchema.JobColumnName:
            column_data = PullRequestJobSchema.ColumnData()
            column_data.title = column_name.value
            column_data.dataIndex = column_name.name
            column_data.key = column_name.name
            table_data.columns.append(column_data.__dict__)

        key = 0
        for k, group in component_group:
            row_data = PullRequestJobSchema.JobRowData()
            row_data.key = key
            key += 1
            row_data.component = k
            pr_job_list = list(group)
            pr_job_group = groupby(pr_job_list, key=lambda x: x["status"])
            for job_status, jobs in pr_job_group:
                if job_status == "SUCCESS":
                    row_data.passed = len(list(jobs))
                elif job_status == "FAILURE":
                    row_data.failed = len(list(jobs))
                elif job_status == "UNSTABLE":
                    row_data.unstable = len(list(jobs))
                elif job_status == "ABORTED":
                    row_data.abort = len(list(jobs))
            row_data.total = (
                row_data.passed + row_data.failed + row_data.unstable + row_data.abort
            )
            row_data.failrate = (
                str(round(row_data.failed / row_data.total * 100, 2)) + "%"
                if row_data.total != 0
                else "NA"
            )

            table_data.data.append(row_data.__dict__)

        return resp.listResp(data=table_data.__dict__)

    except Exception as e:
        print(e)
        return resp.errResp()
