from src.db import DBConnection


def get_experiences():
    experiences = DBConnection('experiences')
    return {
        'experiences': experiences.find()
    }


def get_app_data():
    application = DBConnection('application')
    links = DBConnection('links')

    return {
        'title': application.find()[ 0 ],
        'header': links.find()
    }
