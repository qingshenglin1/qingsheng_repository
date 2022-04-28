import time

from selenium import webdriver
import pytest
import sys
sys.path.append(r"../pageobject")
sys.path.append(r"../Common")
from login_page import *
import project_list_page
import new_project_page
from parse_yml import read_yaml


pro_name1="test_{}".format(time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())))
username1=read_yaml(r"..\Config\redmine.yml","logininfo","username")
password1=read_yaml(r"..\Config\redmine.yml","logininfo","password")
class TestNewProject(object):

    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:81/redmine/login")
    def teardown(self):
        self.driver.quit()
    def test_002_newproject(self):
        LoginScenario(self.driver).login(username1,password1)
        self.driver.get("http://localhost:81/redmine/projects")
        project_list_page.NewProject(self.driver).click_new_project_btn()
        new_project_page.NewProjectScenario(self.driver).new_project(pro_name1)
        text=new_project_page.ChuangJianProject(self.driver).ger_success_message()
        assert text=="创建成功"

if __name__=="__main__":
    pytest.main(['-s','test_002_newproject.py','--html=./report.html'])