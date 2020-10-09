from src.db import DBConnection


def get_projects():
    project_db = DBConnection('projects')

    return {
        'projects': project_db.find()
    }


def insert_projects(projects):
    project_db = DBConnection('projects')

    for project in projects:
        project_db.update(project, 'projectId')

    return {
        'projects': project_db.find()
    }


def remove_projects(projects):
    project_db = DBConnection('projects')

    project_db.delete_all(projects, 'projectId')

    return {
        'projects': project_db.find()
    }
