from src.db import DBConnection
from src.models.company import Company


def get_companies():
    techDb = DBConnection('companies')

    return {
        'companies': techDb.find()
    }


def insert_companies(companies):
    techDb = DBConnection('companies')

    new_list = [ Company.load_from_json(company) for company in companies ]

    for company in new_list:
        company.is_valid() and techDb.update(company.to_json(), 'companyId')

    return {
        'companies': techDb.find()
    }


def remove_companies(companies):
    techDb = DBConnection('companies')

    techDb.delete_all(companies, 'companyId')

    return {
        'companies': techDb.find()
    }
