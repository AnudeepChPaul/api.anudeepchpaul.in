import pymongo
from flask import Blueprint, request

from src.controllers.auth_service import requires_super_admin
from src.db import DBConnection
from src.db.company import get_companies, insert_companies, remove_companies

company_service = Blueprint('company_service', __name__,
                            url_prefix='/resume/api/company_service')


@company_service.route('/get_companies')
def get_all_skills():
    return get_companies()


@company_service.route('/update', methods=[ 'PUT' ])
@requires_super_admin
def update_or_create_skills():
    return insert_companies(request.json.get('companies', None))


@company_service.route('/delete', methods=[ 'DELETE' ])
@requires_super_admin
def delete_skills():
    return remove_companies(request.args.get('companyIds').split(','))


def configure_company_table():
    companyDb = DBConnection('companies')
    companyDb.collection.create_indexes([ pymongo.IndexModel([ ("companyId", pymongo.ASCENDING) ], unique=True) ])
