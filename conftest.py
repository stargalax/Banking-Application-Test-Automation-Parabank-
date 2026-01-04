import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():
    options = Options()
    # options.add_argument("--headless")  # enable if needed
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    yield driver
    driver.quit()
