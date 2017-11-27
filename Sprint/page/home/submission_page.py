from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
import utility.custom_logger as cl
import logging
import time



class Submisson(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    # Locators
    _submitProject_cta = ".//a[contains(text(),'SUBMIT PROJECT')]"
    _updateProject_cta = ".//a[contains(text(),'UPDATE PROJECT')]"
    _projectTitle = ".//input[@placeholder = 'Project title']"
    _theme = ".//*[@id='id_theme']"
    _projectDesc = ".//textarea[@placeholder='Project description']"
    _tags = ".//div[@class= 'react-tags__selected']"
    _submit_cta = ".//span[contains(text(),'Submit')]"
    _edit_pencil = ".//div[@class='float-right edit_button']/a/div"
    #_edit_pencil = ".//*[@id='sprint-root']/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/a/div"

    # Verify the state of phase and make submission


    def make_Submission(self,hackathon_status=1):
        if hackathon_status ==1:
          self.project_Submission_Status()
        else:
            ("Two phase hackathon")


    # Project submission form
    def project_Submission_Status(self):
        if self.get_element(self._submitProject_cta)is not None:
            print("Submitting....")
            self.get_element(self._submitProject_cta).click()
            self.submission_form()
        elif self.get_element(self._updateProject_cta) is not None:
            print("Updating Submission")
            self.get_element(self._updateProject_cta).click()
            time.sleep(5)
            self.get_element(self._edit_pencil).click()
            time.sleep(3)
            #Not able to click on edit
            #self.get_element(self._projectTitle).send_keys("My Test project Updated")

        else:
            print("Element Not found")

    def submission_form(self):
        self.get_element(self._projectTitle).send_keys("My Test project Updated")
        self.get_element(self._theme).send_keys("General")
        self.get_element(self._projectDesc).send_keys("It's a project about Innovation")
        self.get_element(self._submit_cta).click()





    '''# Idea submission Phase
    def idea_Submission(self):'''
