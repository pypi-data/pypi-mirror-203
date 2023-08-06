from pydantic import BaseModel


class ErrorCode(BaseModel):
    code: int
    msg: str
    data: dict = None


ERROR_500 = ErrorCode(code=500, msg="系统异常，请稍后再试").dict()
ERROR_202 = ErrorCode(code=202, msg="创建失败，数据已存在").dict()


def dictResp(code=0, msg="ok", data=None):
    return dict(code=code, msg=msg, data={} or data)


def listResp(code=0, msg="ok", data=None):
    return dict(code=code, msg=msg, data=[] or data)


def errResp(code=1, msg="failed", data=None):
    return dict(code=code, msg=msg, data={} or data)
