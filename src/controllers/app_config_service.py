from flask import Blueprint, request

from src.db.application import configure_application_config_table, get_app_data, get_app_data_from_config, \
    set_app_configs, get_all_app_config

app_config_service = Blueprint('app_config_service', __name__, url_prefix='/resume/api/app_config_service')


@app_config_service.route('/initialize')
def initialize():
    return get_app_data()


@app_config_service.route('/all')
def get_all_config():
    return get_all_app_config()


@app_config_service.route('')
def get_config():
    return get_app_data_from_config(request.args.get('configName'))


@app_config_service.route('/update', methods=[ 'PUT' ])
def save_app_configuration():
    return set_app_configs(request.json)


def configure_app_service():
    configure_application_config_table()
