from selenium.webdriver.common.by import By

#页面元素查找
class ProjectListPage(object):
    def __init__(self,driver):
        self.driver=driver
    #查找新建项目按钮
    def find_new_project_btn(self):
        return self.driver.find_element(By.LINK_TEXT,"新建项目")

class NewProject(object):
    def __init__(self,driver):
        self.projectlistpage=ProjectListPage(driver)
    #点击新建项目按钮
    def click_new_project_btn(self):
        self.projectlistpage.find_new_project_btn().click()
