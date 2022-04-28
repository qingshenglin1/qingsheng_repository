from selenium import webdriver
import pytest
import sys
sys.path.append(r"../pageobject")
sys.path.append(r"../Common")
from login_page import *
from read_excel import read_excel
from parse_yml import read_yaml

host=read_yaml(r"..\Config\redmine.yml",'websites','host')
data=read_excel(r"..\Data\login_data.csv")
url="http://"+host+"/redmine/login"
print(url)
# data=[['admin','123456','0'],['root','0718xjaqs','1']]
@pytest.mark.parametrize(("username","password","status"),data)
class TestLogin():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
    def teardown(self):
        self.driver.quit()

    def test_001_login(self,username,password,status):
        LoginScenario(self.driver).login(username,password)
        if status=='0':
            text=LoginOpen(self.driver).get_fail_info()
            assert text=="无效的用户名或密码"
        elif status=='1':
            text=LoginOpen(self.driver).get_username()
            assert username in text
        else:
            print("参数化状态只能输入0或者1")

