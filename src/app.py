from flask import Flask, Blueprint
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app_route = Blueprint('app', __name__, url_prefix='/app')


@app_route.route('/initialize')
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


@app_route.route('/skills')
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


app.register_blueprint(app_route)

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=5000,
        debug=True
    )
