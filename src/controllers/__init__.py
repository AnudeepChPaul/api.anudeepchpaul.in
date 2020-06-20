from .resume_service import resume_service
from .app_service import app_service


def initiate_routes(app):
    app.register_blueprint(resume_service)
    app.register_blueprint(app_service)
