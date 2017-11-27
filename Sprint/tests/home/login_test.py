from page.home.login_page import login_page
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Logintest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,):
        self.lg = login_page(self.driver)

    @pytest.mark.run(order=1)
    def test_InvalidLogin(self):
        self.lg.verify_Login("#id", "#pwd")
        result = self.lg.verify_login_fail()
        assert result == True

    @pytest.mark.run(order=2)
    def test_ValidLogin(self):
        self.lg.verify_Login("#id", "#pwd")
        result = self.lg.verify_login_pass()
        assert result == True
