from selenium.webdriver.common.by import By

#页面元素查找
class LoginPage(object):
    def __init__(self,driver):
        self.driver=driver
    #查找登录框
    def find_username(self):
        return self.driver.find_element(By.ID,"username")
    #查找密码框
    def find_password(self):
        return self.driver.find_element(By.ID,"password")
    #点击登录按钮元素
    def find_btn(self):
        return self.driver.find_element(By.ID,"login-submit")
    #登录成功显示用户名
    def find_login_name(self):
        return self.driver.find_element(By.ID,"loggedas")
    #登录失败提示
    def find_fail_info(self):
        return self.driver.find_element(By.ID,"flash_error")
 #页面元素操作
class LoginOpen(object):
    def __init__(self,driver):
        self.login_page=LoginPage(driver)
    #输入用户名
    def enter_username(self,username):
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)
    #输入密码
    def enter_password(self,password):
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)
    #点击登录按钮
    def click_login_btn(self):
        self.login_page.find_btn().click()
    #获取登录成功的用户名
    def get_username(self):
        return self.login_page.find_login_name().text
    #获取登录失败的信息
    def get_fail_info(self):
        return self.login_page.find_fail_info().text
#登录业务场景
class LoginScenario(object):
    def __init__(self,driver):
        self.login_scen=LoginOpen(driver)
    def login(self,username,password):
        self.login_scen.enter_username(username)
        self.login_scen.enter_password(password)
        self.login_scen.click_login_btn()