from page.home.new_hackathon import new_Hackathon
from page.home.login_page import login_page
import time
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Create_HackathonTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lg = login_page(self.driver)
        self.new = new_Hackathon(self.driver)

    @pytest.mark.run(order=1)
    def test_create(self):
        # enter your id and pwd
        self.lg.verify_Login("#id", "#pwd")
        time.sleep(3)
        self.new.create_Hackathon("Test_Hackathon_05")
        time.sleep(5)
        self.new.edit_Hackathon()

        '''for i in range(1,101):
            name = "Test_"+str(i)
            print(name)
            self.new.create_Hackathon(name)
            #print("Clicked on Get started link")'''

