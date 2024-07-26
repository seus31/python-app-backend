from backend.service.user_service import get_user_logic
from backend.service.user_service import post_user_logic


def get_user():
    return get_user_logic()


def post_user():
    return post_user_logic()
