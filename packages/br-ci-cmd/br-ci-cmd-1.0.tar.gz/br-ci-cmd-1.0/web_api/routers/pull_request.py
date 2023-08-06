from crypt import methods
from datetime import datetime, timedelta
from itertools import groupby

from flask import Blueprint, request

from ..handles import component as ComponentHandle
from ..handles import pull_request as PullRequestHandle
from ..schemas import component as ComponentSchema
from ..schemas import pull_request as PullRequestSchema
from ..utils import resp

router = Blueprint("Merge_Request", __name__, url_prefix="/api/pr")

# 新增pull request
@router.route("/add", methods=["post"])
def add_Merge_Request():
    data = request.get_json()
    pr = PullRequestSchema.PullRequest(**data)
    out = PullRequestHandle.add_Merge_Request(pr)
    return resp.dictResp(data=out)


# 更新pull request
@router.route("/update", methods=["put"])
def update_Merge_Request():
    update = PullRequestSchema.UpdatePullRequest(**dict(request.get_json()))
    out = PullRequestHandle.update_pull_reqauest(update)
    return resp.listResp(data=out)


# 获取指定时间段内每天pr的数量和效率的overview
@router.route("/get-pr-overview", methods=["get"])
def get_pr_overview():
    try:
        # 根据查询条件获取pr list
        Merge_Request_list = get_Merge_Request_list_by_condition()

        # 根据创建时间对pr进行排序
        Merge_Request_list = sorted(
            Merge_Request_list, key=lambda pr: get_timestamp(pr["prCreatedTime"])
        )
        # 根据创建时间对pr进行分组
        Merge_Request_group = groupby(
            Merge_Request_list, key=lambda x: x["prCreatedTime"]
        )
        # 字典 key-日期，value-pr数量
        date_created_pr_count_dict = {}
        # 字典 key-日期，value-merged pr数量
        date_merged_pr_dict = {}
        # 字典 key-日期，value-closed pr数量
        date_closed_pr_dict = {}
        # 字典 key-日期，value-closed pr关联的job数量
        date_closed_pr_job_dict = {}
        # 字典 key-日期， value-job数量
        date_job_dict = {}

        for key, group in Merge_Request_group:
            group_list = list(group)
            date_created_pr_count_dict[key] = len(group_list)

            merged_pr_list = [pr for pr in group_list if pr["status"] == "merged"]
            date_merged_pr_dict[key] = len(merged_pr_list)

            closed_pr_list = [pr for pr in group_list if pr["status"] == "closed"]
            date_closed_pr_dict[key] = len(closed_pr_list)

            # 统计closed pr关联的job数量
            for pr in closed_pr_list:
                if key in date_closed_pr_job_dict:
                    date_closed_pr_job_dict[key] += len(pr["jobList"])
                else:
                    date_closed_pr_job_dict[key] = len(pr["jobList"])

            # 统计pr关联的job数量
            for pr in group_list:
                if key in date_job_dict:
                    date_job_dict[key] += len(pr["jobList"])
                else:
                    date_job_dict[key] = len(pr["jobList"])

        # 根据pr creatd的日期对 pr group进行排序
        sorted_date_created_pr_count_dict = [
            (k, date_created_pr_count_dict[k])
            for k in sorted(date_created_pr_count_dict.keys())
        ]

        # 构造返回数据
        bar_graph_data = PullRequestSchema.BarGraphData()
        result_data = PullRequestSchema.ResultData()
        result_data.name = "pr次数"
        merged_result_data = PullRequestSchema.ResultData()
        merged_result_data.name = "pr成功率"
        closed_result_data = PullRequestSchema.ResultData()
        closed_result_data.name = "pr无效率"
        merged_divided_by_job_result_data = PullRequestSchema.ResultData()
        merged_divided_by_job_result_data.name = " pr合并率"
        closed_job_divided_by_job_result_data = PullRequestSchema.ResultData()
        closed_job_divided_by_job_result_data.name = "CI资源浪费率"

        for key, value in sorted_date_created_pr_count_dict:
            bar_graph_data.xAxis.append(key)

            # pr created数量
            result_data.data.append(value)
            # pr job数量
            if key in date_job_dict:
                job_amount = date_job_dict[key]
            else:
                job_amount = 0
            # merged pr 数量
            if key in date_merged_pr_dict:
                merged_pr_amount = date_merged_pr_dict[key]
            else:
                merged_pr_amount = 0
            merged_result_data.data.append(
                str(round(merged_pr_amount / value * 100, 2)) + "%"
                if value != 0
                else "NA"
            )
            merged_divided_by_job_result_data.data.append(
                str(round(merged_pr_amount / job_amount * 100, 2)) + "%"
                if job_amount != 0
                else "NA"
            )

            # closed pr 数量
            if key in date_closed_pr_dict:
                closed_pr_amount = date_closed_pr_dict[key]
            else:
                closed_pr_amount = 0
            closed_result_data.data.append(
                str(round(closed_pr_amount / value * 100, 2)) + "%"
                if value != 0
                else "NA"
            )

            # closed pr 关联的job数量
            if key in date_closed_pr_job_dict:
                closed_pr_job_amount = date_closed_pr_job_dict[key]
            else:
                closed_pr_job_amount = 0
            closed_job_divided_by_job_result_data.data.append(
                str(round(closed_pr_job_amount / job_amount * 100, 2)) + "%"
                if job_amount != 0
                else "NA"
            )

        bar_graph_data.data.append(result_data.__dict__)
        bar_graph_data.data.append(merged_result_data.__dict__)
        bar_graph_data.data.append(closed_result_data.__dict__)
        bar_graph_data.data.append(merged_divided_by_job_result_data.__dict__)
        bar_graph_data.data.append(closed_job_divided_by_job_result_data.__dict__)

        return resp.listResp(data=bar_graph_data.__dict__)
    except Exception as e:
        print(e)
        return resp.errResp()


def get_Merge_Request_list_by_condition():
    date = (
        request.args.get("date")
        if request.args.get("date")
        else datetime.now().strftime("%Y-%m-%d")
    )
    day_span = request.args.get("daySpan", 7, int) if request.args.get("daySpan") else 7
    query = PullRequestSchema.QueryPullRequest()
    query.component = request.args.get("component")
    current_time = datetime.strptime(date, "%Y-%m-%d")
    query.endTime = current_time + timedelta(days=1)
    query.startTime = query.endTime - timedelta(days=day_span)
    query_component = ComponentSchema.QueryComponent()
    query_component.parentComponent = request.args.get("parentComponent")
    result = ComponentHandle.get_component_list_by_parent(query_component)
    component_list = []
    for c_list in result:
        for c in c_list:
            component_list.append(c.name)
    query.components = component_list
    # 根据查询条件获取pr list
    Merge_Request_list = PullRequestHandle.get_Merge_Request_list_and_job_list(query)
    result_list = []
    for pr in Merge_Request_list:
        pr["prCreatedTime"] = pr["prCreatedTime"].strftime("%Y-%m-%d")
        result_list.append(pr)
    return result_list


# 时间转换
def get_timestamp(date):
    return datetime.strptime(date, "%Y-%m-%d").timestamp()


# pr详情table
@router.route("/detail", methods=["get"])
def get_Merge_Request_detail():
    try:
        # 根据查询条件获取pr list
        result = get_Merge_Request_list_and_related_job_list()
        Merge_Request_list = []
        for pr in result:
            Merge_Request_list.append(pr)

        table_data = PullRequestSchema.PRTableData()
        for column_name in PullRequestSchema.PRColumnName:
            column_data = PullRequestSchema.ColumnData()
            column_data.title = column_name.value
            column_data.dataIndex = column_name.name
            column_data.key = column_name.name
            table_data.columns.append(column_data.__dict__)

        key = 0
        for pr in Merge_Request_list:
            row_data = PullRequestSchema.PRRowData()
            row_data.key = key
            key += 1
            row_data.pullRequestNumber = pr["pullRequestNumber"]
            row_data.name = pr["pullRequestName"]
            job_list = pr["jobList"]
            for job in job_list:
                if "status" in job:
                    if job["status"] == "SUCCESS":
                        row_data.passed += 1
                    elif job["status"] == "FAILURE":
                        row_data.failed += 1
                    elif job["status"] == "UNSTABLE":
                        row_data.unstable += 1
                    elif job["status"] == "ABORTED":
                        row_data.abort += 1
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


# PR-红榜/黑榜, 个人 merged/failed 效率 TOP n
@router.route("most-efficient-user", methods=["get"])
def most_efficient_user():
    try:
        # 根据查询条件获取pr list以及关联的job
        result = get_Merge_Request_list_and_related_job_list()
        Merge_Request_list = []
        for pr in result:
            pr["relatedJobAmount"] = len(pr["jobList"]) if "jobList" in pr else 0
            Merge_Request_list.append(pr)

        top = request.args.get("top", 10, type=int) if request.args.get("top") else 10
        type = (
            request.args.get("type", "merged", type=str)
            if request.args.get("type")
            else "merge"
        )

        # 根据pr创建者分组
        Merge_Request_group = groupby(
            Merge_Request_list, key=lambda x: (x["prCreatedBy"])
        )

        # 返回参数类型 PRTableData
        table_data = PullRequestSchema.PRTableData()

        # 如果要查询的是用户红榜（merged pr/总job数）
        if type == "merge":
            user_merge_rate_list = []
            for key, group in Merge_Request_group:
                user_merge_rate = PullRequestSchema.UserMergRate()
                sub_group = groupby(list(group), key=lambda x: (x["status"]))
                user_merge_rate.user = key
                for k, g in sub_group:
                    list_g = list(g)
                    if k == "merged":
                        user_merge_rate.mergedPR = len(list_g)
                    for pr in list_g:
                        user_merge_rate.totalPRJOb += pr["relatedJobAmount"]
                user_merge_rate.passRateFloat = (
                    round(user_merge_rate.mergedPR / user_merge_rate.totalPRJOb, 4)
                    if user_merge_rate.totalPRJOb != 0
                    else 0
                )
                user_merge_rate.passRate = (
                    str(
                        round(
                            user_merge_rate.mergedPR / user_merge_rate.totalPRJOb * 100,
                            2,
                        )
                    )
                    + "%"
                    if user_merge_rate.totalPRJOb != 0
                    else "NA"
                )
                user_merge_rate_list.append(user_merge_rate.__dict__)

            user_merge_rate_list.sort(key=lambda x: x["passRateFloat"], reverse=True)

            # 构建返回参数
            key = 0
            for s in user_merge_rate_list:
                row_data = PullRequestSchema.UserRowData()
                row_data.key = key
                key += 1
                row_data.ranking = key
                row_data.name = s["user"]
                row_data.merged = s["mergedPR"]
                row_data.total = s["totalPRJOb"]
                row_data.passrate = s["passRate"]
                table_data.data.append(row_data.__dict__)

                if row_data.ranking == top:
                    break

        # 如果要查询的是用户黑榜（Unstable+Abort jobs/job总数）
        elif type == "failure":
            user_failed_rate_list = []
            for key, group in Merge_Request_group:
                user_failed_rate = PullRequestSchema.UserFailRate()
                user_failed_rate.user = key
                for pr in list(group):
                    job_list = pr["jobList"]
                    for job in job_list:
                        if "status" in job and (
                            job["status"] == "UNSTABLE" or job["status"] == "ABORTED"
                        ):
                            user_failed_rate.failedPR += 1
                    user_failed_rate.totalPRJOb += len(job_list)

                user_failed_rate.failedRateFloat = (
                    round(user_failed_rate.failedPR / user_failed_rate.totalPRJOb, 4)
                    if user_failed_rate.totalPRJOb != 0
                    else 0
                )
                user_failed_rate.failedRate = (
                    str(
                        round(
                            user_failed_rate.failedPR
                            / user_failed_rate.totalPRJOb
                            * 100,
                            2,
                        )
                    )
                    + "%"
                    if user_failed_rate.totalPRJOb != 0
                    else "NA"
                )
                user_failed_rate_list.append(user_failed_rate.__dict__)

            user_failed_rate_list.sort(key=lambda x: x["failedRateFloat"], reverse=True)

            # 构建返回参数
            key = 0
            for s in user_failed_rate_list:
                row_data = PullRequestSchema.UserRowData()
                row_data.key = key
                key += 1
                row_data.ranking = key
                row_data.name = s["user"]
                row_data.failed = s["failedPR"]
                row_data.total = s["totalPRJOb"]
                row_data.failedrate = s["failedRate"]
                table_data.data.append(row_data.__dict__)

                if row_data.ranking == top:
                    break

        # 构建返回参数列名称
        for column_name in PullRequestSchema.UserColumnName:
            column_data = PullRequestSchema.ColumnData()
            column_data.title = column_name.value
            column_data.dataIndex = column_name.name
            column_data.key = column_name.name
            table_data.columns.append(column_data.__dict__)

        return resp.listResp(data=table_data.__dict__)
    except Exception as e:
        print(e)
        return resp.errResp()


# 单个PR失败率TOP3, 单个pr的jobs的Unstable+Abort/jobs总数
@router.route("most-efficient-pr", methods=["get"])
def most_efficient_Merge_Request():
    try:
        # 根据查询条件获取pr list以及关联的job
        result = get_Merge_Request_list_and_related_job_list()
        Merge_Request_list = []
        for pr in result:
            pr["relatedJobAmount"] = len(pr["jobList"]) if "jobList" in pr else 0
            Merge_Request_list.append(pr)

        top = request.args.get("top", 3, type=int) if request.args.get("top") else 3

        # 根据pullLink分组
        Merge_Request_group = groupby(Merge_Request_list, key=lambda x: (x["pullLink"]))

        # 返回参数类型 PRTableData
        table_data = PullRequestSchema.PRTableData()

        # 如果要查询的是用户红榜（merged pr/总job数）
        pr_list = []
        for pr in Merge_Request_list:
            pr_row_data = PullRequestSchema.PullRequestRowData()
            pr_row_data.name = pr["pullRequestName"]
            pr_row_data.prURL = pr["pullLink"]
            pr_row_data.total = len(pr["jobList"]) if "jobList" in pr else 0
            job_list = pr["jobList"]
            failed = 0
            for job in job_list:
                if "status" in job and (
                    job["status"] == "FAILURE" or job["status"] == "ABORTED"
                ):
                    failed += 1
            pr_row_data.failed = failed

            pr_row_data.failedrateFloat = (
                round(pr_row_data.failed / pr_row_data.total, 4)
                if pr_row_data.total != 0
                else 0
            )
            pr_row_data.failedrate = (
                str(round(pr_row_data.failed / pr_row_data.total * 100, 2)) + "%"
                if pr_row_data.total != 0
                else "NA"
            )
            pr_list.append(pr_row_data.__dict__)

        # 根据失败率排序
        pr_list.sort(key=lambda x: x["failedrateFloat"], reverse=True)

        # 返回参数类型 PRTableData
        table_data = PullRequestSchema.PRTableData()

        # 构建返回参数
        key = 0
        ranking = 0
        last_failed_rate = -1
        for pr in pr_list:
            if pr["failedrate"] != last_failed_rate:
                ranking += 1
                # 如果排名大于要求的top数，结束循环
                if ranking > top:
                    break
            last_failed_rate = pr["failedrate"]
            pr["key"] = key
            key += 1
            pr["ranking"] = ranking
            table_data.data.append(pr)

        # 构建返回参数列名称
        for column_name in PullRequestSchema.PullRequestColumnName:
            column_data = PullRequestSchema.ColumnData()
            column_data.title = column_name.value
            column_data.dataIndex = column_name.name
            column_data.key = column_name.name
            table_data.columns.append(column_data.__dict__)

        return resp.listResp(data=table_data.__dict__)

    except Exception as e:
        print(e)
        return resp.errResp()


# 根据条件获取pr和关联的pr job list
def get_Merge_Request_list_and_related_job_list():
    try:
        # 获取参数
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
        result = PullRequestHandle.get_Merge_Request_list_and_job_list(query)
        return result
    except Exception as e:
        print(e)
        return resp.errResp()
