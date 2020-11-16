from suds.client import Client
from suds import WebFault
from model.project import Project
import json
import os.path


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_project_list(self):
        file_name = (os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'target.json'))
        with open(file_name) as f:
            info = json.load(f)
        user = info["webadmin"]
        username = user["username"]
        password = user["password"]
        url = info["web"]
        name_url = url["baseUrl"]
        name_projects = []
        client = Client("%s/api/soap/mantisconnect.php?wsdl" % name_url)
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            for element in projects:
                name = element.name
                name_projects.append(Project(name=name))
            return list(name_projects)
        except WebFault:
            return False

