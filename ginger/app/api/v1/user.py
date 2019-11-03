from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User
from app.libs.error_code import NotFound

api = Redprint('user')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    # validate token legal
    # validate token expiration
    user = User.query.get_or_404(uid)
    return 'i am zw'