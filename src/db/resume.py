from src.db import Database
import json
from flask import jsonify


def get_skills():
    skills = Database('skills')

    return {
        'skills': {
            'list': skills.find()
        }
    }, 200


def get_experiences():
    experiences = Database('experiences')
    return {
        'experiences': {
            'list': experiences.find()
        }
    }


def get_app_data():
    application = Database('application')
    links = Database('links')

    return {
        'title': application.find()[0],
        'header': {
            'list': links.find(),
        }
    }, 200
