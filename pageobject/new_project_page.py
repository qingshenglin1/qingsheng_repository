from selenium.webdriver.common.by import By


class NewProjectPage(object):
    def __init__(self,driver):
        self.driver=driver
    #查找项目名称
    def find_project_name(self):
        return self.driver.find_element(By.ID,"project_name")
    #查找创建按钮
    def find_chuangjian_btn(self):
        return self.driver.find_element(By.NAME,"commit")

    #查找新建成功提示系信息
    def fin_success_message(self):
        return self.driver.find_element(By.ID,"flash_notice")

class ChuangJianProject(object):
    def __init__(self,driver):
        self.newprojectpage=NewProjectPage(driver)
    def enter_project_name(self,pro_name):
        self.newprojectpage.find_project_name().send_keys(pro_name)
    def click_chuangjian_btn(self):
        self.newprojectpage.find_chuangjian_btn().click()
    #返回新建成功提示信息
    def ger_success_message(self):
        return self.newprojectpage.fin_success_message().text
#创建对象场景
class NewProjectScenario(object):
    def __init__(self,driver):
        self.chuangjian_project=ChuangJianProject(driver)
    #创建对象场景
    def new_project(self,pro_name):
        self.chuangjian_project.enter_project_name(pro_name)
        self.chuangjian_project.click_chuangjian_btn()

