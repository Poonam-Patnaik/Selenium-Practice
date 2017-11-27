from page.home.UserFlow_page import user_Jorney
from page.home.login_page import login_page
import time
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Create_HackathonTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lg = login_page(self.driver)
        self.user_jrny = user_Jorney(self.driver)


    # Hackathon Over
    @pytest.mark.run(order=1)
    def test_register(self):
        #enter ur id and pwd
        self.lg.verify_Login("#id", "#pwd")
        self.driver.get("https://www.hackerearth.com/sprints/test_regn-v2/")
        time.sleep(3)
        self.user_jrny.user_Register()
        time.sleep(5)
    #Live Hackathon
    @pytest.mark.run(order=2)
    def test_register(self):
        # enter ur id and pwd
        self.lg.verify_Login("#id", "#pwd")
        BaseUrl = "https://www.hackerearth.com/sprints/unisys-hackathon-2020/"
        self.driver.get(BaseUrl)
        time.sleep(3)
        #hacakthon_phase = self.lg.get_hackathon_phase(BaseUrl)
        self.user_jrny.user_Register()
        time.sleep(5)
        self.user_jrny.user_Submission()

