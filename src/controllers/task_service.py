from flask import Blueprint, request

from src.controllers.auth_service import requires_super_admin
from src.db.task import configure_tasks, delete_selected_tasks, get_all_tasks, new_task, update_task

task_service = Blueprint('task_service', __name__,
                         url_prefix='/resume/api/task_service')


@task_service.route('/get_tasks', methods=[ 'GET' ])
@requires_super_admin
def get_tasks():
    return get_all_tasks(page=request.args.get('page'), page_size=request.args.get('pageSize'))


@task_service.route('/new', methods=[ 'POST' ])
@requires_super_admin
def save_new_task():
    return new_task(request.json)


@task_service.route('/update', methods=[ 'PUT' ])
@requires_super_admin
def update_existing_task():
    return update_task(request.json)


@task_service.route('/delete', methods=[ 'DELETE' ])
@requires_super_admin
def delete_all_tasks():
    taskIds = request.args.get('taskIds', None)

    if taskIds is not None:
        return delete_selected_tasks(taskIds.split(","))
    else:
        return delete_selected_tasks(None)


def configure_tasks_table():
    configure_tasks()
