from flask import Blueprint
from src.db.resume import get_app_data

app_service = Blueprint('app_service', __name__, url_prefix='/resume/api/app_service')


@app_service.route('/initialize')
def initialize():
    return get_app_data()