import uuid

from src.models.base import BaseModel


class User(BaseModel):
    def __init__(self, userId, username, password, roleId, token):
        self.userId = userId or str(uuid.uuid5(uuid.NAMESPACE_DNS, username))
        self.username = username
        self.password = password
        self.roleId = roleId or 'USER'
        self.token = token

    def to_json(self, secure=False):
        return dict({
            'userId': self.userId,
            'username': self.username,
            'password': None if secure else self.password,
            'roleId': self.roleId,
            'token': self.token
        })

    @staticmethod
    def load_from_json(data):
        return User(
            data.get('userId'),
            data.get('username'),
            data.get('password'),
            data.get('roleId'),
            data.get('token')
        )
        pass

    @staticmethod
    def get_key():
        return 'userId'
