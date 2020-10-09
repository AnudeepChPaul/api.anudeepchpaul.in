from src.db import DBConnection


def get_technologies():
    techDb = DBConnection('technologies')

    return {
        'technologies': techDb.find()
    }


def insert_technologies(skills):
    techDb = DBConnection('technologies')

    for skill in skills:
        # if skill.get('_id', None):
        #     skill.pop('_id')

        techDb.update(skill, 'techId')

    return {
        'technologies': techDb.find()
    }


def remove_technologies(skills):
    techDb = DBConnection('technologies')

    techDb.delete_all(skills, 'techId')

    return {
        'technologies': [ ]
    }
