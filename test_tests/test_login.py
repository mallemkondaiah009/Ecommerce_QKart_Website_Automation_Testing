import pytest
from test_pages.login_page import LoginPage

@pytest.mark.usefixtures("init_driver")
class TestQKartLogin:

    def test_login_user(self):
        # Open the application URL
        self.driver.get("https://crio-qkart-frontend-qa.vercel.app/")

        # Initialize LoginPage object
        login_page = LoginPage(self.driver)

        # Interact with login page elements
        login_page.click_login()
        login_page.enter_username("roronoa zoro")
        login_page.enter_password("123456789")
        login_page.click_login_submit()

