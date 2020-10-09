import pymongo
from flask import Blueprint, request

from src.controllers.auth_service import requires_super_admin
from src.db import DBConnection
from src.db.technology import get_technologies, insert_technologies, remove_technologies

technology_service = Blueprint('technology_service', __name__,
                               url_prefix='/resume/api/technology_service')


@technology_service.route('/get_technologies')
def get_all_skills():
    return get_technologies()


@technology_service.route('/update', methods=[ 'PUT' ])
@requires_super_admin
def update_or_create_skills():
    return insert_technologies(request.json.get('skills', None))


@technology_service.route('/delete', methods=[ 'DELETE' ])
@requires_super_admin
def delete_skills():
    return remove_technologies(request.args.get('techIds').split(','))


def configure_technology_config_table():
    techDb = DBConnection('technologies')
    techDb.collection.create_indexes([ pymongo.IndexModel([ ("techId", pymongo.ASCENDING) ], unique=True) ])
