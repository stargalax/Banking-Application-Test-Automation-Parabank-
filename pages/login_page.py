from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//input[@value='Log In']")
    error_msg = (By.CSS_SELECTOR, ".error")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text
