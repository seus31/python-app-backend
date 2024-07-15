from flask import request
from functools import wraps

def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization", None)
        return func(*args, **kwargs)
    return wrapper
