import werkzeug
from flask import Flask

from .utils.log import Log
from .utils.resp import ERROR_500, errResp


class InsufficientStorage(werkzeug.exceptions.HTTPException):
    code = 500
    description = "Not enough storage space."


def handler_500(e):
    Log.exception(f"500 ERROR:")
    return errResp(**ERROR_500)


def register_error_handler(app: Flask):
    app.register_error_handler(Exception, handler_500)
