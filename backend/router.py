from flask import Blueprint

from controller import task_controller
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


@router.route('/api/v1/users/<int:user_id>', methods=['GET'])
@logger.http_request_logging
@auth.requires_auth
def get_user(user_id):
    return user_controller.get_user(user_id)


@router.route('/api/v1/users/<int:user_id>', methods=['PUT'])
@logger.http_request_logging
@auth.requires_auth
def update_user(user_id):
    return user_controller.update_user(user_id)


@router.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
@logger.http_request_logging
@auth.requires_auth
def delete_user(user_id):
    return user_controller.delete_user(user_id)


@router.route("/api/v1/tasks", methods=['POST'])
@logger.http_request_logging
@auth.requires_auth
def api_v1_tasks_post_task():
    return task_controller.post_task()


@router.route("/api/v1/tasks", methods=['GET'])
@logger.http_request_logging
@auth.requires_auth
def api_v1_tasks_gete_tasks():
    return task_controller.get_tasks()


@router.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
