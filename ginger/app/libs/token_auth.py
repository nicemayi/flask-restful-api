from collections import namedtuple

from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature
from itsdangerous import SignatureExpired
from flask import g
from flask import current_app
from app.libs.error_code import AuthFailed


auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        # samilar to request object
        g.user = user_info
    return True

def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expird', error_code=1003)

    uid = data['uid']
    ac_type = data['type']
    scope = data['is_admin']
    return User(uid=uid, ac_type=ac_type, scope=scope)
