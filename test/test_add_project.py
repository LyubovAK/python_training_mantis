from model.project import Project


def test_add_project(app):
    old_projects = app.project.get_project_list()
    app.project.add_project(Project(name="test"))
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
