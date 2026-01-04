from pages.login_page import LoginPage
from pages.transfer_page import TransferPage

def test_fund_transfer(setup):
    LoginPage(setup).login("john", "demo")
    transfer = TransferPage(setup)
    transfer.transfer_funds("100")
    assert "Transfer Complete!" in transfer.get_success_message()
