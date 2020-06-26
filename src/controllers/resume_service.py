from flask import Flask, Blueprint
from src.db.resume import get_skills, get_experiences

resume_service = Blueprint('resume_service', __name__,
                           url_prefix='/resume/api/resume_service')


@resume_service.route('/skills')
def skills():
    return get_skills()


@resume_service.route('/experiences')
def experiences():
    return get_experiences()
