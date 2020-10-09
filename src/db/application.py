import pymongo

from src.db import DBConnection


def configure_application_config_table():
    application = DBConnection('application')
    application.collection.create_indexes([ pymongo.IndexModel([ ("configName", pymongo.ASCENDING) ], unique=True) ])


def with_observer(fn):
    def subscribe(*args, **kwargs):
        return fn(*args, **kwargs)

    return subscribe


def get_app_data():
    application = DBConnection('application')
    links = DBConnection('links')

    try:
        app_config = application.find()
        result = dict()
        for config in app_config:
            result[ config.get('configName') ] = config.get('value')
    except:
        result = None

    return {
        'applicationConfig': result,
        'header': {
            'list': links.find(),
        }
    }


def get_app_data_from_config(config):
    application = DBConnection('application')

    try:
        app_config = application.find({ 'configName': config })
        result = dict()
        for config in app_config:
            result[ config.get('configName') ] = config.get('value')
    except:
        result = None

    return {
        'applicationConfig': result
    }


def get_all_app_config():
    application = DBConnection('application')

    try:
        app_config = application.find()
        result = dict()
        for config in app_config:
            result[ config.get('configName') ] = config.get('value')
    except:
        result = None

    return {
        'applicationConfig': result
    }


@with_observer
def set_app_configs(app_config):
    application = DBConnection('application')
    try:
        for key in app_config.keys():
            config = dict({
                'configName': key,
                'value': app_config.get(key)
            })
            application.update(config, 'configName')
    except:
        return {
            'appConfig': False
        }

    return {
        'appConfig': True
    }
