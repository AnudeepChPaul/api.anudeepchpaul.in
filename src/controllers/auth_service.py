import json
import uuid
from datetime import timedelta
from functools import wraps

from flask import Blueprint, Response, request
from passlib.hash import sha256_crypt

from src.db.user import UserNotFound, WrongPasswordError, get_user_by_username
from src.helpers.token_service import Token

auth_service = Blueprint('auth_service', __name__,
                         url_prefix='/api/auth_service')


class AuthError(Exception):
    def __init__(self, error):
        self.error = error


def get_client_ip():
    return request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ[ 'REMOTE_ADDR' ]


def get_token_auth_header():
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({ "code": "authorization_header_missing",
                          "description":
                              "Authorization header is expected" })
    parts = auth.split()
    if parts[ 0 ].lower() != "bearer":
        raise AuthError({ "code": "invalid_header",
                          "description":
                              "Authorization header must start with"
                              " Bearer" }, 401)

    elif len(parts) == 1:
        raise AuthError({ "code": "invalid_header",
                          "description": "Token not found" })

    elif len(parts) > 2:
        raise AuthError({ "code": "invalid_header",
                          "description":
                              "Authorization header must be"
                              " Bearer token" })

    return Token(parts[ 1 ])


def validate_token():
    payload = get_token_auth_header().decode_token()

    if payload.get('origin') != request.origin or \
            payload.get('is_secure') != request.is_secure or \
            payload.get('username') != request.headers.get('X-User-Name', None) or \
            payload.get('client_ip') != get_client_ip():
        raise AuthError('HEADERS_MISSING')

    return True


def if_super_admin_token():
    payload = get_token_auth_header().decode_token()

    if payload.get('origin') != request.origin or \
            payload.get('is_secure') != request.is_secure or \
            payload.get('username') != request.headers.get('X-User-Name', None) or \
            payload.get('client_ip') != get_client_ip() or \
            payload.get('permissions').index('SUPERADMIN') == -1:
        raise AuthError('HEADERS_MISSING')

    return True


def requires_super_admin(f):
    @wraps(f)
    def if_super_admin(*args, **kwargs):
        if_super_admin_token()
        print('token validated for {}'.format(request.url))

        return f(*args, **kwargs)

    return if_super_admin


def validate_user_with_credentials(req):
    req_body = req.json

    try:
        selected_user = get_user_by_username(req_body.get('username'), n=0)

        if not sha256_crypt.verify(req_body.get('password'), selected_user.get('password')):
            raise WrongPasswordError()

        for key in list([ '_id', 'password' ]):
            selected_user.pop(key)

    except WrongPasswordError as error:
        return {
            'REASON': error.message
        }

    except UserNotFound as error:
        return {
            'REASON': error.message
        }

    except:
        return {
            'REASON': 'UNEXPECTED_ERROR'
        }

    return {
        'USER': selected_user
    }


@auth_service.route('/login', methods=[ 'POST' ])
def login_user():
    result = validate_user_with_credentials(request)
    user = result.get('USER', None)

    if not user:
        return {
                   'LOGGED_IN': False,
                   'REASON': result.get('REASON')
               }, 401

    user[ 'userId' ] = str(uuid.uuid5(uuid.NAMESPACE_DNS, user.get('username')))
    token = Token(payload=dict({
        'origin': request.origin,
        'is_secure': request.is_secure,
        'client_ip': get_client_ip(),
        'username': user[ 'username' ],
        'permissions': user.get('permissions')
    }))
    user[ 'token' ] = token.token
    return Response(json.dumps(result), status=200)


@auth_service.route('/validate_token', methods=[ 'GET' ])
def try_to_validate_token():
    validate_token()

    resp = Response(json.dumps({
        'validToken': True
    }))
    return resp
