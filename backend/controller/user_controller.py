from service.user_service import get_users_logic
from service.user_service import post_user_logic
from service.user_service import get_user_logic
from service.user_service import update_user_logic


def get_users():
    return get_users_logic()


def post_user():
    return post_user_logic()


def get_user(user_id):
    return get_user_logic(user_id)


def update_user(user_id):
    return update_user_logic(user_id)
