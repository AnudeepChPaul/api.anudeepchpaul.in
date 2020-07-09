from flask import Flask, Blueprint, request
from src.db.logger import post_performance_logs, post_url_hits

logger_service = Blueprint('logger_service', __name__,
                           url_prefix='/resume/api/logger_service')


@logger_service.route('/performance', methods=['GET'])
def save_performance():
    return post_performance_logs(request)