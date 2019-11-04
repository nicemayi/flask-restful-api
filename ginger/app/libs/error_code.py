from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


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


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005


class ServerError(APIException):
    code = 500
    error_code = 999