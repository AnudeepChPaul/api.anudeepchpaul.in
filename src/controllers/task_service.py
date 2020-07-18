from flask import Flask, Blueprint, request
from src.db.tasks import get_all_tasks, new_task, update_task, configure_tasks, delete_selected_tasks
from bson import json_util
import json

task_service = Blueprint('task_service', __name__,
                         url_prefix='/resume/api/task_service')


@task_service.route('/all', methods=['GET'])
def get_tasks():
    return get_all_tasks()


@task_service.route('/new', methods=['POST'])
def save_new_task():
    return new_task(request.json)


@task_service.route('/update', methods=['PUT'])
def update_existing_task():
    return update_task(request.json)


@task_service.route('/delete', methods=['DELETE'])
def delete_all_tasks():
    taskIds = request.args.get('taskIds', None)

    if taskIds is not None:
        return delete_selected_tasks(taskIds.split(","))
    else:
        return delete_selected_tasks(None)


def configure_task_service():
    configure_tasks()
