from model.project import Project
import random


def test_delete_project(app, config):
    if len(app.soap.get_project_list(app.base_url, config["webadmin"]["username"], config["webadmin"]["password"])) == 0:
        app.project.add_project(Project(name="Project_for_delete"))
    old_projects = app.soap.get_project_list(app.base_url, config["webadmin"]["username"], config["webadmin"]["password"])
    project = random.choice(old_projects)
    app.project.delete_some_project(project)
    new_projects = app.soap.get_project_list(app.base_url, config["webadmin"]["username"], config["webadmin"]["password"])
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.sorted_name) == sorted(new_projects, key=Project.sorted_name)
