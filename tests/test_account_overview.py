from pages.login_page import LoginPage
from pages.account_page import AccountPage

def test_account_overview(setup):
    LoginPage(setup).login("john", "demo")
    account = AccountPage(setup)
    assert account.is_account_visible()
