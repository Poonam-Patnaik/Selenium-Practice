from base.selenium_driver import SeleniumDriver
from page.home.Register_page import Register
from page.home.submission_page import Submisson
import utility.custom_logger as cl
import logging


class user_Jorney(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)


    def user_Register(self):
        regn = Register(self.driver)
        regn.register()


    def user_Submission(self,hackathon_status=1):
        sub = Submisson(self.driver)
        sub.make_Submission(hackathon_status=1)

    '''def submission(self):
        sub = Submisson(self.driver)'''


    '''
      Condition to verify sigle phase / two phase
      if !single:
            idea.idea_submission()
       prj.project_submission()
            
      
       def project_submission(self):
         #project page object
        # project submission method
    '''



