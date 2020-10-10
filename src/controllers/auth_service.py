import json
from functools import wraps

from flask import Blueprint, request
from passlib.hash import pbkdf2_sha256

from src.db.user import UserNotFound, WrongPasswordError, get_user_by_username, save_user
from src.helpers.token_service import Token
from src.models.ApiResponse import ApiResponse
from src.models.user import User

auth_service = Blueprint('auth_service', __name__,
                         url_prefix='/api/auth_service')


class AuthError(Exception):
    def __init__(self, error):
        self.message = 'AUTHENTICATION_FAILURE'
        self.error = error


def get_client_ip():
    return request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ['REMOTE_ADDR']


def get_token_auth_header():
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                         "description":
                             "Authorization header is expected"})
    parts = auth.split()
    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                         "description":
                             "Authorization header must start with"
                             " Bearer"})

    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                         "description": "Token not found"})

    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                         "description":
                             "Authorization header must be"
                             " Bearer token"})

    return Token(parts[1])


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
            payload.get('role') == 'SUPER_ADMIN':
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

    selected_user = get_user_by_username(req_body.get('username'), n=0)

    if not pbkdf2_sha256.verify(req_body.get('password'), selected_user.get('password')):
        raise WrongPasswordError()

    # for key in list(['_id', 'password']):
    #     selected_user.pop(key)

    return User.load_from_json(selected_user)


@auth_service.route('/login', methods=['POST'])
def login_user():
    try:
        user = validate_user_with_credentials(request)

    except UserNotFound as error:
        return {
                   'LOGGED_IN': False,
                   'REASON': error.message
               }, 401
    except WrongPasswordError as error:
        return {
                   'LOGGED_IN': False,
                   'REASON': error.message
               }, 401
    except:
        return {
                   'LOGGED_IN': False,
                   'REASON': 'UNEXPECTED_ERROR'
               }, 401

    user.token = Token(payload=dict({
        'origin': request.origin,
        'is_secure': request.is_secure,
        'client_ip': get_client_ip(),
        'username': user.username,
        'role': user.roleId
    })).token

    return {'USER': user.to_json(secure=True)}


@auth_service.route('/validate_token', methods=['GET'])
def try_to_validate_token():
    validate_token()

    resp = ApiResponse(json.dumps({
        'validToken': True
    }))
    return resp


@auth_service.route('/signup', methods=['POST'])
def register_new_user():
    try:
        user = validate_user_with_credentials(request)

    except AuthError as error:
        return {
                   'LOGGED_IN': False,
                   'REASON': 'USER_ALREADY_EXISTS'
               }, 401

    except WrongPasswordError as error:
        user = None
    except UserNotFound as error:
        user = None

    if not user:
        body = request.json

        encrypted_pwd = pbkdf2_sha256.using().hash(body.get('password'))

        user = User(None, body.get('username'), encrypted_pwd, None, None)

        user.roleId = 'SUPER_ADMIN' if user.username == 'achandrapaul' else None

        token = Token(payload=dict({
            'origin': request.origin,
            'is_secure': request.is_secure,
            'client_ip': get_client_ip(),
            'username': user.username,
            'role': user.roleId
        }))

        user.token = token.token

        save_user(user)

    return {'USER': user.to_json(secure=True)}
