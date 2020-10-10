import json
import random
import os

# import gevent
from flask import Flask, Response
from flask_cors import CORS

from src import controllers
from src.controllers.auth_service import AuthError
from src.helpers.token_service import InvalidTokenError
from src.configurations import config

app = Flask(__name__)

CORS(app)


# @app.after_request
# def after_request(res):
#     if not request.origin:
#         mode = 'DIRECT_SERVER_CALL'
#     elif request.origin.find('localhost') or request.origin.find('127.0.0.1'):
#         mode = 'DEVELOPMENT'
#     else:
#         mode = 'PRODUCTION'
#
#     LOG = {
#         'req_path': request.full_path,
#         'origin': request.origin,
#         'host_url': request.host_url,
#         'endpoint': request.endpoint,
#         'authorization': request.authorization,
#         'service_name': request.blueprint,
#         'time': datetime.now(),
#         'mode': mode
#     }
#     p = Process(target=post_url_hits, args=(LOG,))
#     p.start()
#     print('before_request executed!')
#     return res


@app.route('/')
def root():
    return ''


if os.environ.get('DEBUG_MODE', False):
    @app.route('/config')
    def get_config():
        return {
            'debug': config.bool('DEBUG_MODE'),
            'db_root': config.str('DB_ROOT_NAME'),
            'mongo_url': config.str('MONGO_DB_CONNECTION_URL')
        }


def event_stream():
    while True:
        event_data = {
            'notifications': 25
        }
        event_type = ['info', 'error', 'skills',
                      'experience'][random.randint(0, 3)]
        event_id = random.randint(100000000000, 9999999999999)

        yield 'id: {}\nevent: {}\ndata: {}\n\n'.format(event_id, event_type, json.dumps(event_data))
        # gevent.sleep(0.5)

#
# @app.route("/stream/<string:stream_id>")
# def stream(stream_id):
#     response = Response(event_stream(), headers={
#         'Content-Type': 'text/event-stream',
#         'Cache-Control': 'no-cache',
#         'Access-Control-Allow-Origin': '*',
#         'Content-Security-Policy': "default-src '*'",
#         'X-STREAM-ID': stream_id
#     })
#     return response


# Initiating all the routes
controllers.initiate_routes(app)


@app.errorhandler(AuthError)
def on_auth_error(ex):
    response = json.dumps({
        'SUCCESS': False,
        'REASON': ex.error
    })
    return response, 401


@app.errorhandler(InvalidTokenError)
def on_invalid_token_error(ex):
    response = json.dumps({
        'SUCCESS': False,
        'REASON': ex.error
    })
    return response, 401


controllers.configure_collections()
