from flask import Blueprint

from src.db.resume import get_experiences

resume_service = Blueprint('resume_service', __name__,
                           url_prefix='/resume/api/resume_service')


@resume_service.route('/experiences')
def experiences():
    return get_experiences()
