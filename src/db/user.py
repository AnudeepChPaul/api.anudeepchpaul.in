import pymongo

from src.db import DBConnection


class WrongPasswordError(ValueError):
    def __init__(self, message='INVALID_PASSWORD'):
        self.message = message
        super().__init__(self.message)


class UserNotFound(ValueError):
    def __init__(self, message='USER_NOT_FOUND'):
        self.message = message
        super().__init__(self.message)


def configure_users_table():
    users = DBConnection('users')
    users.collection.create_indexes([ pymongo.IndexModel([ ("username", pymongo.TEXT) ], unique=True) ])


def get_user_by_username(username, n=None):
    db = DBConnection('users')
    user = db.find({ 'username': username })

    if not len(user):
        raise UserNotFound()

    if n is None:
        return user
    else:
        return user[ int(n) ]
