import json

import pymongo
from bson import json_util
from pymongo.errors import DuplicateKeyError

from src.db import Database

WORK_TYPES = {
    'TODO': 'TODO',
    'IN_PROGRESS': 'IN_PROGRESS',
    'DONE': 'DONE',
}


def configure_tasks():
    tasks = Database('tasks')
    tasks.collection.create_index([ ("taskId", pymongo.ASCENDING) ], unique=True)


def get_all_tasks():
    tasks = Database('tasks')

    return {
        'tasks': tasks.find()
    }


def new_task(task):
    tasks = Database('tasks')

    try:
        return {
            'tasks': [ tasks.save(task) ],
            'error': [ ]
        }
    except DuplicateKeyError as error:
        return {
            'tasks': [ json.loads(json_util.dumps(task)) ],
            'error': error.args
        }


def update_task(task):
    db = Database('tasks')

    WORK_PROGRESS_WORKFLOW = [
        WORK_TYPES.get('TODO'),
        WORK_TYPES.get('IN_PROGRESS'),
        WORK_TYPES.get('DONE'),
    ]

    workflow_index = WORK_PROGRESS_WORKFLOW.index(task.get('type'))
    workflow_direction = task.get('workflowDirection')

    try:
        task.pop('workflowDirection')
        task.pop('_id')
    except:
        pass
    finally:
        if workflow_direction == 'NEXT' and workflow_index != len(WORK_PROGRESS_WORKFLOW):
            task[ 'type' ] = WORK_PROGRESS_WORKFLOW[ workflow_index + 1 ]

        if workflow_direction == 'PREV' and workflow_index != 0:
            task[ 'type' ] = WORK_PROGRESS_WORKFLOW[ workflow_index - 1 ]

    return {
        'tasks': [ db.update(task, 'title') ]
    }


def delete_selected_tasks(tasks):
    db = Database('tasks')

    # try:
    db.delete_all(tasks, 'taskId')
    # finally:
    return {
        'tasks': [ ]
    }
