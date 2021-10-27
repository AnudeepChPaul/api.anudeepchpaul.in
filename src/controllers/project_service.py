import pymongo
from flask import Blueprint, request

from src.controllers.auth_service import requires_super_admin
from src.db import DBConnection
from src.db.projects import get_projects, insert_projects, remove_projects, update_projects
from flask_cors import CORS

project_service = Blueprint('project_service', __name__,
                            url_prefix='/resume/api/project_service')

CORS(project_service)


@project_service.route('/get_projects')
def get_all_projects():
    return get_projects()


@project_service.route('/update', methods=['POST'])
# @requires_super_admin
def update_or_create_projects():
    return insert_projects(request.json.get('projects', None))


@project_service.route('/update/<project_id>', methods=['PUT'])
# @requires_super_admin
def update_single_project(project_id):
    return update_projects(request.json.get('projects', None))


@project_service.route('/delete/<project_id>', methods=['DELETE'])
# @requires_super_admin
def delete_projects(project_id):
    return remove_projects(project_id.split(','))


def configure_project_config_table():
    projects_db = DBConnection('projects')
    projects_db.collection.create_indexes(
        [pymongo.IndexModel([("projectId", pymongo.ASCENDING)], unique=True)])
