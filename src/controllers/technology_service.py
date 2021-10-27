import pymongo
from flask import Blueprint, request
from flask_cors import CORS

from src.controllers.auth_service import requires_super_admin
from src.db import DBConnection
from src.db.technology import get_technologies, insert_technology, update_technology, remove_technologies

technology_service = Blueprint('technology_service', __name__,
                               url_prefix='/resume/api/technology_service')

CORS(technology_service)


@technology_service.route('/get_technologies')
def get_all_skills():
    return get_technologies()


@technology_service.route('/update', methods=['POST'])
# @requires_super_admin
def update_or_create_skills():
    return insert_technology(request.json.get('technologies', None))


@technology_service.route('/update/<techId>', methods=['PUT'])
# @requires_super_admin
def update_skill(techId):
    return update_technology(request.json.get('technologies', None))


@technology_service.route('/delete/<tech_id>', methods=['DELETE'])
# @requires_super_admin
def delete_skills(tech_id):
    return remove_technologies(tech_id.split(','))


def configure_technology_config_table():
    techDb = DBConnection('technologies')
    techDb.collection.create_indexes(
        [pymongo.IndexModel([("techId", pymongo.ASCENDING)], unique=True)])
