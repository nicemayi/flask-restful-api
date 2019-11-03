from werkzeug.exceptions import HTTPException


class ClientTypeError(HTTPException):
    code = 400
    description = (
        'client is invalid'
    )


class EmailRegisterError(HTTPException):
    code = 400
    description = (
        'you can not use this email to register'
    )