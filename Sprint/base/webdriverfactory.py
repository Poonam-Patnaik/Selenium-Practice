import traceback
from selenium import webdriver

class webDriver_Fcatory():
    def __init__(self,browser):
        self.browser = browser

    def get_WebDriverInstance(self):
        baseURL = "https://www.hackerearth.com/sprint/"

        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=r'D:\geckodriver-v0.16.1-win64\geckodriver.exe')
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.get(baseURL)
        return driver