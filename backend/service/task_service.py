from flask import make_response, request, jsonify
from model.task import Task, TaskSchema


def post_task_logic():
    data = request.json
    task_name = data.get('task_name')
    status = data.get('status')

    if not task_name or not status:
        return make_response(
            jsonify({
                'code': 400,
                'error': 'Missing required fields'
            })
        )
    new_task = Task(task_name=task_name, status=status).create_task()
    task_schema = TaskSchema(many=False)

    return make_response(
        jsonify({
            'code': 201,
            'task': task_schema.dump(new_task)
        })
    )


def get_tasks_logic():
    tasks = Task.get_task_list()
    task_schema = TaskSchema(many=True)
    return make_response(jsonify({
        'code': 200,
        'tasks': task_schema.dump(tasks)
    }))


def get_task_logic(task_id):
    task = Task.query.get_or_404(task_id)
    task_schema = TaskSchema()
    return make_response(jsonify({
        'code': 200,
        'task': task_schema.dump(task)
    }))


def delete_task_logic(task_id):
    task = Task.query.get_or_404(task_id)
    task.delete_task()

    return make_response(jsonify({
        'code': 200,
        'message': 'Task deleted successfully'
    }))
