from flask import Flask, Blueprint

resume_service = Blueprint('resume_service', __name__,
                           url_prefix='/resume/api/resume_service')


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
                    'text': "React",
                    'value': '85',
                    'actionKey': "react",
                },
                {
                    'text': "EXT Js",
                    'value': '85',
                    'actionKey': "extjs",
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
                {
                    'text': "Flask",
                    'value': '85',
                    'actionKey': "flask",
                },
            ],
        }
    }


@resume_service.route('/experiences')
def experiences():
    return {
        'experiences': {
            'list': [{
                "order": 1,
                "companyName": 'InQuest Technologies',
                "duration": '2016-01-07 to 2018-05-05',
                "designation": "Mid Level Software Developer"
            }, {
                "order": 2,
                "companyName": 'Manhattan Associates',
                "duration": '2018-07-09 to current',
                "designation": "Sr. Software Engineer"
            }]
        }
    }
