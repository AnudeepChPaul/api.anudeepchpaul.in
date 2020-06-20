from flask import Blueprint

app_service = Blueprint('app_service', __name__, url_prefix='/resume/api/app_service')


@app_service.route('/initialize')
def initialize():
    return {
        'title': "Anudeep Chandra Paul's Resume",
        'header': {
            'list': [
                  {'text': "About me", 'actionKey': "about_me"},
                  {'text': "Skills", 'actionKey': "skills"},
                  {'text': "Experience", 'actionKey': "experience"},
                  {'text': "Package", 'actionKey': "pay_scale"},
                  {'text': "Contact", 'actionKey': "contact"}
            ],
        },
    }