import time
from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        self.open_manage_proj_page()
        self.open_manage_proj_create_page()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        #time.sleep(5)
        self.open_manage_proj_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']")


    def open_manage_proj_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()


    def open_manage_proj_create_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("manage_proj_create_page.php"):
            wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_proj_page()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("tr.row-1"):
                name = element.find_element_by_xpath(".//td[1]").text
                self.project_cache.append(Project(name=name))
            for element in wd.find_elements_by_css_selector("tr.row-2"):
                name = element.find_element_by_xpath(".//td[1]").text
                self.project_cache.append(Project(name=name))
        return list(self.project_cache)



