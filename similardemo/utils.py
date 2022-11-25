# -*- coding: utf-8 -*-
'''
@Time    :   2022-11-23 19:13:35
@File    :   utils.py
@author  :   youker-Shawn
@Desc    :   通用工具
'''
from typing import Optional


def api_response(
    code: int = 200,
    msg: str = "",
    result: Optional[dict] = None,
    status: str = "success",
):
    """统一的后端接口返回内容格式"""
    # 默认值
    ret = {
        "code": code,
        "status": status,
        "message": msg,
        "result": result if result else {},
    }

    if str(code).startswith("2") or str(code).startswith("3"):  # 2XX 3XX
        ret["status"] = "success"
    elif str(code).startswith("4"):  # 4XX
        ret["status"] = "error"
    elif str(code).startswith("5"):  # 5XX
        ret["status"] = "fail"
    else:
        pass  # 其他自定义code，默认为success

    return ret
