import pytest
from test_pages.Logout import LogoutPage


@pytest.mark.usefixtures("login")
class TestLogout:

    def test_logout(self):
        logout_page = LogoutPage(self.driver)
        logout_page.logout()
