from pages.login_page import LoginPage

def test_login_valid(setup):
    login = LoginPage(setup)
    login.login("john", "demo")
    assert "Accounts Overview" in setup.page_source


def test_login_invalid(setup):
    login = LoginPage(setup)
    login.login("wrong", "wrong")
    assert "The username and password could not be verified" in login.get_error_message()
