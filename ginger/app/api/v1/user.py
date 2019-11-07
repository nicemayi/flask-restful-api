from flask import jsonify
from flask import g

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User
from app.libs.error_code import NotFound
from app.libs.error_code import DeleteSuccess
from app.libs.error_code import AuthFailed
from app.models.base import db


api = Redprint('user')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # validate token legal
    # validate token expiration
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    # filter_by不会把status=0的找出来
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    # g(基变量是线程隔离的)
    # 但是必须要@auth.login_required
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()