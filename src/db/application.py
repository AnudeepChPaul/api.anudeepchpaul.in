from src.db import Database
import json


def get_app_data():
    application = Database('application')
    links = Database('links')

    return {
        'title': application.find()[0],
        'header': {
            'list': links.find(),
        }
    }, 200
