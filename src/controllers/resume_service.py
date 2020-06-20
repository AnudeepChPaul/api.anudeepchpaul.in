from flask import Flask, Blueprint

resume_service = Blueprint('resume_service', __name__, url_prefix='/resume/api/resume_service')


@resume_service.route('/skills')
def skills():
    return {
        'skills': {
            'list': [
                {
                    'text': "Python",
                    'value': '85',
                    'actionKey': "python",
                },
                {
                    'text': "Html & Css",
                    'value': '80',
                    'actionKey': "html_and_css",
                },
                {
                    'text': "Javascript",
                    'value': '90',
                    'actionKey': "javascript",
                },
                {
                    'text': "Flask",
                    'value': '85',
                    'actionKey': "flask",
                },
                {
                    'text': "React",
                    'value': '85',
                    'actionKey': "react",
                },
                {
                    'text': "Node js",
                    'value': '70',
                    'actionKey': "node",
                },
                {
                    'text': "express",
                    'value': '70',
                    'actionKey': "express",
                },
            ],
        }
    }