from service.task_service import post_task_logic
from service.task_service import get_tasks_logic
from service.task_service import get_task_logic


def post_task():
    return post_task_logic()


def get_tasks():
    return get_tasks_logic()


def get_task(task_id):
    return get_task_logic(task_id)
