from model.project import Project
import random


def test_delete_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.add_project(Project(name="Project_for_delete"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_some_project(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.sorted_name) == sorted(new_projects, key=Project.sorted_name)
