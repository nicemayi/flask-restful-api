class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api += other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module += other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden += other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self


class UserScope(Scope):
    allow_api = ['v1.user+get_user']
    forbidden = ['v1.user+super_get_user']

    def __init__(self):
        self + AdminScope()


class AdminScope(Scope):
    allow_api = ['v1.user+super_get_user']

    def __init__(self):
        self + UserScope()


def is_in_scope(scope, endpoint):
    # 反射，根据类的名字动态创建对象
    # globals
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    return False
