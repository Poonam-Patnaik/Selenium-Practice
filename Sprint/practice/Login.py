from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Logintest():
    driver = webdriver.Firefox(executable_path=r'D:\geckodriver-v0.16.1-win64\geckodriver.exe')
    driver.get("https://www.hackerearth.com/sprint/")
    #driver.maximize_window()
    driver.implicitly_wait(3)

    loginLink = driver.find_element(By.XPATH, ".//*[@id='header-primary']/div/ul/li[4]/a")
    loginLink.click()

    emailField = driver.find_element(By.XPATH, ".//*[@id='id_email']")
    emailField.send_keys("poonam@hackerearth.com")

    passwordField = driver.find_element(By.XPATH, ".//*[@id='id_password']")
    passwordField.send_keys("poonit0902")

    loginButton = driver.find_element(By.CSS_SELECTOR, ".button.btn-large.btn-blue.full-width.medium-margin.weight-700.mp-login-cta")
    loginButton.click()


    currenturl  = driver.current_url
    print(currenturl)
    if currenturl == "https://www.hackerearth.com/sprints/admin/" :
        print("Login Successful")
        driver.find_element(By.XPATH, ".//*[@id='hacker-dd-icon']/a/div/i").click()
        driver.find_element(By.XPATH, ".//*[@id='hacker-box']/ul/a[11]/li").click()
    else:
        print("Login Failed")
    driver.quit()