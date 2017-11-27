from selenium.webdriver.common.by import By
import utility.custom_logger as cl
import logging

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
    def get_Title(self):
        return self.driver.title

    def get_element(self, locator, locator_type=By.XPATH):
        element = None
        try:

            element = self.driver.find_element(locator_type, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locator_type)
        except:
            self.log.info("Element Not Found with locator: " + locator + " and  locatorType: " + locator_type)
        return element
    def get_hackathon_phase(self,url):

        phase = 1
        idea_phase = self.driver.find_element(By.XPATH,".//div[@class = 'idea-phase time-location-specification']")
        if idea_phase is None:
            print("Its single phase")
        else:
            phase = 2
            print("Its 2 Phase")
        return phase






