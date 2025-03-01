from functools import wraps
from flask import g,redirect,url_for
def login_required(func):
    @wraps (func)
    def inner(*args,**kwargs):
        if g.user:
            #第一个用来接收任意数量的位置参数，第二个用来接收任意数量的关键字参数
            return func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))
    return inner