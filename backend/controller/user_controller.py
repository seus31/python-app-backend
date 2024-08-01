from service.user_service import get_users_logic
from service.user_service import post_user_logic


def get_users():
    return get_users_logic()


def post_user():
    return post_user_logic()
