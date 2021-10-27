from src.db import DBConnection


def get_technologies():
    techDb = DBConnection('technologies')

    return {
        'technologies': techDb.find()
    }


def insert_technology(skill):
    techDb = DBConnection('technologies')

    techDb.update(skill, 'techId')

    return {
        'technologies': techDb.find({
            'techId': skill.get('techId', None)
        })
    }


def update_technology(skill):
    techDb = DBConnection('technologies')

    techDb.update(skill, 'techId')

    return {
        'technologies': techDb.find({
            'techId': skill.get('techId', None)
        })
    }


def remove_technologies(skills):
    techDb = DBConnection('technologies')

    techDb.delete_all(skills, 'techId')

    return {
        'technologies': []
    }
