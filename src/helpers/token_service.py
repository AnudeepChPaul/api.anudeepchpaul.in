from jose import jwt
from src.configurations import config

SECRET = config.str('SECRET')
ALGORITHM = config.str('ALGORITHM')


class InvalidTokenError(Exception):
    def __init__(self, error):
        self.error = error


class Token():
    def __init__(self, token=None, payload=None):
        self.token = token or self.create_new_token(payload)

    def create_new_token(self, payload):
        final_payload = payload or dict()
        return jwt.encode(final_payload, SECRET, ALGORITHM)

    def decode_token(self):
        try:
            return jwt.decode(self.token, SECRET, ALGORITHM)

        except jwt.ExpiredSignatureError:
            raise InvalidTokenError({ "code": "token_expired",
                                      "description": "token is expired" })
        except jwt.JWTClaimsError:
            raise InvalidTokenError({ "code": "invalid_claims",
                                      "description":
                                          "incorrect claims,"
                                          "please check the audience and issuer" })
        except Exception:
            raise InvalidTokenError({ "code": "invalid_header",
                                      "description":
                                          "Unable to parse authentication"
                                          " token." })
