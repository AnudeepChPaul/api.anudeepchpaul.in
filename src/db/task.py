import json

import pymongo
from bson import json_util
from pymongo.errors import DuplicateKeyError

from src.db import DBConnection

WORK_TYPES = {
    'TODO': 'TODO',
    'IN_PROGRESS': 'IN_PROGRESS',
    'DONE': 'DONE',
}


def configure_tasks():
    tasks = DBConnection('tasks')
    tasks.collection.create_indexes([ pymongo.IndexModel([ ("taskId", pymongo.ASCENDING) ], unique=True) ])


def get_all_tasks(page=0, page_size=20):
    tasks = DBConnection('tasks')

    all_tasks = tasks.find_by_page({ }, page=int(page), page_size=int(page_size))

    return {
        'tasks': all_tasks[ 0 ],
        'pageData': {
            'start': all_tasks[ 1 ],
            'end': all_tasks[ 2 ],
            'page': page,
            'size': page_size,
            'total': all_tasks[ 3 ]
        }
    }


def new_task(task):
    tasks = DBConnection('tasks')

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
    db = DBConnection('tasks')

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
    db = DBConnection('tasks')

    # try:
    db.delete_all(tasks, 'taskId')
    # finally:
    return {
        'tasks': [ ]
    }
