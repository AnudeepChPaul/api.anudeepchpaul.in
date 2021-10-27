from src.db import DBConnection


def get_projects():
    project_db = DBConnection('projects')

    return {
        'projects': project_db.find()
    }


def insert_projects(project):
    project_db = DBConnection('projects')

    project_db.update(project, 'projectId')

    return {
        'projects': project_db.find({
            'projectId': project.get('projectId', None)
        })
    }


def update_projects(project):
    project_db = DBConnection('projects')

    project_db.update(project, 'projectId')

    return {
        'projects': project_db.find({
            'projectId': project.get('projectId', None)
        })
    }


def remove_projects(projects):
    project_db = DBConnection('projects')

    project_db.delete_all(projects, 'projectId')

    return {
        'projects': project_db.find()
    }
