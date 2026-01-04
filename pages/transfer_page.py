from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransferPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    transfer_link = (By.LINK_TEXT, "Transfer Funds")
    amount = (By.ID, "amount")
    from_account = (By.ID, "fromAccountId")
    to_account = (By.ID, "toAccountId")
    transfer_btn = (By.XPATH, "//input[@value='Transfer']")
    success_msg = (By.XPATH, "//div[@id='showResult']//h1")

    def transfer_funds(self, amt):
        self.driver.find_element(*self.transfer_link).click()

        self.wait.until(EC.visibility_of_element_located(self.amount)).send_keys(amt)

        from_acc = Select(self.driver.find_element(*self.from_account))
        to_acc = Select(self.driver.find_element(*self.to_account))

        # Select different accounts safely
        from_acc.select_by_index(0)
        to_acc.select_by_index(1)

        self.driver.find_element(*self.transfer_btn).click()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_msg)
        ).text
