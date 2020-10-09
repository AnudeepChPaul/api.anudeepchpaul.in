from src.db import DBConnection
import json
from datetime import datetime
from flask import request


def post_performance_logs(request):
    performance = DBConnection('performance')

    log = {
        'browser': request.user_agent.browser,
        'browser_version': request.user_agent.version,
        'lang': request.user_agent.browser,
        'platform': request.user_agent.platform
    }

    return {
        'log': performance.save(log),
    }, 200


def post_url_hits(log):
    # log = {
    #     'req_path': request.full_path,
    #     'origin': request.origin,
    #     'host_url': request.host_url,
    #     'endpoint': request.endpoint,
    #     'authorization': request.authorization,
    #     'service_name': request.blueprint,
    #     'time': datetime.now(),
    #     'mode': 'None'
    # }
    performance = DBConnection('history')
    performance.save(log)
    print('log posted!')
