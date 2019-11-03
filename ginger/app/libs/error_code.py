from app.libs.error import APIException


class ClientTypeError(APIException):
    code = 400
    description = (
        'client is invalid'
    )
    error_code = 1005
    msg = 'client is invalid'


class EmailRegisterError(APIException):
    code = 400
    description = (
        'you can not use this email to register'
    )
    error_code = 1006
    msg = 'you can not use this email to register'