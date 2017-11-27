from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
import utility.custom_logger as cl
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class new_Hackathon(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)
    # Locators Details :
    _create_link = "+ Create Hackathon"
    #wiszard ele:
    _hackathonName = ".//*[@id='create-sprint-modal']/div[2]/form/div/input"
    _createCTA = ".//*[@id='create-sprint-modal']/div[3]/div[1]/a"
    #5 steps:
    _getStarted = "Get Started"
    #.//*[@id='create-sprint-wizard-modal']/div[2]/a     2. ".//*[@id='get-started']"
    _banner_save = ".//*[@id='save-cover']"
    _team_save = ".//*[@id='wizard-description-submit']"
    _date = ".//*[@id='id_end_date']"
    _time = ".//*[@id='id_end_time']"
    _setdate = "Oct 30, 2018"
    _settime = "02:30 PM"
    _dateTime_CTA = "#wizard-schedule-submit"
        #".//*[@id='wizard-schedule-submit']"
    _theme_Acct = ".//*[@id='create-sprint-wizard-modal']/div[1]/div[3]/div[2]/div[2]/div[2]"
    _theme_digital = ".//*[@id='create-sprint-wizard-modal']/div[1]/div[3]/div[2]/div[3]/div[2] "
    _theme_save ="Save & Continue"
        #".//a[@id='wizard-themes-submit']"
    _loc_save = "#wizard-location-submit"
        #"Check your Hackathon"
    _title = ".//*[@id='create-sprint-wizard-modal']/div[1]/div[1]"

    #locator details for edit:
    _edit = "//a[@class = 'button btn-blue btn-small']/i[@ class='fa fa-pencil']"
    _publish = "//a/i[@ class='fa fa-file-text']"
    _popPublish = ".//*[@class='modal-window small-modal simplemodal-data']/div[3]/a"
        #"Publish"
        #"//a[@clicked = 'Publishing...']"
        #".//*[@id='publish-sprint-modal']/div[3]/a"
        #"Publish"
         #"//*[@id='publish-sprint-modal']/div[3]/a"
        # "Publish"
        #".//a[@class = 'button btn-blue float-right']"


        #".//a[@id='wizard-location-submit']"
        #"#wizard-location-submit"
        #"Check your Hackathon"
        #".//*[@id='wizard-location-submit']"

    def create_Hackathon(self,name):

        self.get_element(self._create_link, By.LINK_TEXT).click()
        time.sleep(2)
        #self.driver.implicitly_wait(3)
        # Fill widzard value
        self.get_element(self._hackathonName).send_keys(name)
        time.sleep(2)
        self.get_element(self._createCTA).click()
        time.sleep(2)
        ele = self.get_element(self._getStarted, By.LINK_TEXT)
        time.sleep(2)
        ele.click()
        self.get_element(self._banner_save).click()
        time.sleep(2)
        self.get_element(self._team_save).click()
        time.sleep(2)
        self.get_element(self._date).send_keys(self._setdate)
        self.get_element(self._date).click()
        self.get_element(self._time).send_keys(self._settime)
        self.get_element(self._time).click()
        scd_ele = self.get_element(self._dateTime_CTA, By.CSS_SELECTOR)
        time.sleep(2)
        scd_ele.click()
        ele_theme = self.get_element(self._theme_save, By.LINK_TEXT)
        print(ele_theme)
        ele_theme.click()
        print("clicked on theme")
        time.sleep(3)
        ele_loc = self.get_element(self._loc_save, By.CSS_SELECTOR)
        print(ele_loc)
        ele_loc.click()

    def edit_Hackathon(self):
        self.get_element(self._edit).click()
        time.sleep(2)


        '''self.get_element(self._publish).click()
        time.sleep(2)
        pop = self.get_element(self._popPublish)

        print(pop)
        #pop.click()
        print("clicked on publish")'''

















    '''def create_Hackthon(self):
        self.get_element(self._create_link, By.LINK_TEXT).click()
        self.driver.implicitly_wait(3)
        #widzard
        self.get_element(self._hackathonName).send_keys("Test_Hack101")
        self.get_element(self._createCTA).click()
        #self.driver.implicitly_wait(50)
        time.sleep(2)
        self.get_element(self._wiz_close).click()

        #self.driver.find_element(By.LINK_TEXT, "Get Started")
        #send_keys(Keys.ENTER)
        ele = self.get_element(self._getStarted,By.LINK_TEXT)
        #ele = self.driver.find_element(By.LINK_TEXT, "Get Started")
        time.sleep(2)
        ele.click()
        self.get_element(self._banner_save).click()
        time.sleep(2)
        self.get_element(self._team_save).click()
        time.sleep(2)
        self.get_element(self._date).send_keys(self._setdate)
        self.get_element(self._date).click()
        self.get_element(self._time).send_keys(self._settime)
        scd_ele = self.get_element(self._dateTime_CTA,By.CSS_SELECTOR)
        time.sleep(2)
        scd_ele.click()
        print("test")
        ele_theme = self.get_element(self._theme_save,By.CSS_SELECTOR)
        print(ele_theme)
        ele_theme.click()
        print("clicked on theme")



        time.sleep(2)
        copy = self.get_element(self._title).text()
        print(copy)
        ele_loc =self.get_element(self._loc_save,By.LINK_TEXT)
        print(ele_loc)
        ele_loc.click()'''













