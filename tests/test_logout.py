from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_logout(setup):
    LoginPage(setup).login("john", "demo")
    setup.find_element(By.LINK_TEXT, "Log Out").click()
    assert "Customer Login" in setup.page_source
