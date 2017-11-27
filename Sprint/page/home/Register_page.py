from base.selenium_driver import SeleniumDriver
import utility.custom_logger as cl
import logging
import time
from selenium.webdriver.common.by import By

class Register(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    _register_Cta = "//a[contains(text(),'REGISTER NOW')]"
    _addInfo_submit = ".//input[@class = 'button btn-green submit-btn inline-block weight-700']"
    _skill_skip = ".//div[@class = 'align-center caps margin-top-50']/a"
    _live_tag = ".//div[@class = 'event-title']/span"
    _update_cta = ".//a[contains(text(),'UPDATE PROJECT')]"
    _submit_project = ".//a[@href = '/sprints/test_hackathon_05-39/dashboard/02df538/submission/']"


    def register(self):
        time.sleep(3)
        hackathon_status = self.get_element(self._live_tag)


        if hackathon_status is None:
            print("Hackathon Over can't Register")
        else:
            regn_cta = self.get_element(self._register_Cta)
            if regn_cta is None:
                print("User Registered")

            else:
                print(regn_cta)
                regn_cta.click()
                time.sleep(3)
                self.add_info()


    def add_info(self):
        time.sleep(3)
        addInfo= self.get_element(self._addInfo_submit)
        addInfo.click()
        time.sleep(3)
        skill = self.get_element(self._skill_skip)
        skill.click()


