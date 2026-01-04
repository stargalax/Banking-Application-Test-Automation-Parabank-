from selenium.webdriver.common.by import By

class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    accounts_table = (By.ID, "accountTable")

    def is_account_visible(self):
        return self.driver.find_element(*self.accounts_table).is_displayed()
