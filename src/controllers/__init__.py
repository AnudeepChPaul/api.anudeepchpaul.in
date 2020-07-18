from .resume_service import resume_service
from .app_service import app_service
from .logger_service import logger_service
from .task_service import task_service, configure_task_service


def initiate_routes(app):
    app.register_blueprint(resume_service)
    app.register_blueprint(app_service)
    app.register_blueprint(logger_service)
    app.register_blueprint(task_service)


def configure_collections():
    configure_task_service()
