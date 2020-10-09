from .app_config_service import app_config_service, configure_app_service
from .auth_service import auth_service
from .company_service import configure_company_table, company_service
from .logger_service import logger_service
from .project_service import project_service, configure_project_config_table
from .resume_service import resume_service
from .task_service import configure_tasks_table, task_service
from .technology_service import configure_technology_config_table, technology_service
from ..db.user import configure_users_table


def initiate_routes(app):
    service_list = [
        auth_service,
        resume_service,
        app_config_service,
        logger_service,
        task_service,
        technology_service,
        company_service,
        project_service
    ]

    for service in service_list:
        app.register_blueprint(service)


def configure_collections():
    configure_tasks_table()
    configure_app_service()
    configure_technology_config_table()
    configure_users_table()
    configure_company_table()
    configure_project_config_table()
