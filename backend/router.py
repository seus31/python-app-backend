from flask import Blueprint
from controller import user_controller
from logging import config
from json import load
import auth
import logger

router = Blueprint('router', __name__)

with open("./config/logging.json", "r", encoding="utf-8") as f:
  config.dictConfig(load(f))


@router.route("/api/v1/users", methods=['GET'])
@logger.http_request_logging
@auth.requires_auth
def api_v1_users_get_user_list():
    return user_controller.get_users()


@router.route("/api/v1/users", methods=['POST'])
@logger.http_request_logging
@auth.requires_auth
def api_v1_users_post_user():
    return user_controller.post_user()


@router.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
