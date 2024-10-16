import pytest
from test_pages.register_page import RegisterPage


@pytest.mark.usefixtures("init_driver")
class TestQKartRegistration:

    def test_register_user(self):
        # Open the application URL
        self.driver.get("https://crio-qkart-frontend-qa.vercel.app/")

        # Initialize RegisterPage object
        register_page = RegisterPage(self.driver)

        # Interact with registration page elements
        register_page.click_register()
        register_page.enter_username("roronoa zoro")
        register_page.enter_password("123456789")
        register_page.enter_confirm_password("123456789")
        register_page.click_register_now()

