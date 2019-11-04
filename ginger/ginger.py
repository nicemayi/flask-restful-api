from app import create_app
from app.libs.error import APIException
from werkzeug.exceptions import HTTPException


app = create_app()

@app.errorhandler(Exception)
def frameword_error(e):
    # e could be the following:
    # APIException
    # HTTPException
    # Exception
    if isinstance(e, APIException):
        return e
    elif isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # return APIException()
        raise e


if __name__ == "__main__":
    app.run(debug=True)