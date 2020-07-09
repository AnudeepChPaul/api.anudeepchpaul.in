from flask import Flask, Blueprint, request
from flask_cors import CORS
import src.controllers as controllers
from src.db.logger import post_url_hits
import concurrent.futures
from multiprocessing import Process
from datetime import datetime


app = Flask(__name__)

CORS(app)

# @app.before_request
# def before_request():
#     post_url_hits(request)

# @app.before_request
# def before_request():
#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         executor.map(post_url_hits, [])
#     print('before_request executed!')


@app.after_request
def after_request(res):
    if not request.origin:
        mode = 'DIRECT_SERVER_CALL'
    elif request.origin.find('localhost') or request.origin.find('127.0.0.1'):
        mode = 'DEVELOPMENT'
    else:
        mode = 'PRODUCTION'

    LOG = {
        'req_path': request.full_path,
        'origin': request.origin,
        'host_url': request.host_url,
        'endpoint': request.endpoint,
        'authorization': request.authorization,
        'service_name': request.blueprint,
        'time': datetime.now(),
        'mode': mode
    }   
    p = Process(target=post_url_hits, args=(LOG,))
    p.start()
    print('before_request executed!')
    return res


controllers.initiate_routes(app)
