from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
import utility.custom_logger as cl
import logging

class login_page(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    #Locators
    _loginlink = ".//*[@id='header-primary']/div/ul/li[4]/a"
    _id = ".//*[@id='id_email']"
    _pwd= ".//*[@id='id_password']"
    _logincta = ".button.btn-large.btn-blue.full-width.medium-margin.weight-700.mp-login-cta"
    _usermenu = ".//*[@id='hacker-dd-icon']/a/div/i"
    _sprint_opt = "Sprint Dashboard"
    _dashboard_title = "Sprint Dashboard | HackerEarth"
    _login_page_title = "HackerEarth Recruit | Log In | HackerEarth"


    def click_LoginLink(self):
        self.get_element(self._loginlink).click()


    def verify_Login(self,id='',pwd=''):
        try:
            self.click_LoginLink()
            self.get_element(self._id).clear()
            self.get_element(self._id).send_keys(id)
            self.get_element(self._pwd).send_keys(pwd)
            self.get_element(self._logincta,By.CSS_SELECTOR).click()
            '''self.get_element(self._usermenu).click()
            self.get_element(self._sprint_opt,By.LINK_TEXT).click()
            print("done")'''

        except:
            self.log.info("Login failed")

    def verify_login_pass(self):
        #currenturl = self.driver.current_url
        current_title = self.get_Title()
        if current_title == self._dashboard_title:
            self.log.info("Login Successful")
        return True

    def verify_login_fail(self):
        #currenturl = self.driver.current_url
        current_title = self.get_Title()
        if current_title == self._login_page_title:
            self.log.info("Login Fail")
        return True