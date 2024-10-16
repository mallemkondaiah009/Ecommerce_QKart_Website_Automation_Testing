import pytest
from test_pages.Privacy_Policy_Page import PrivacyPolicyPage
from test_pages.Aboutus_Page import AboutUsPage
from test_pages.Contactus_Page import ContactUsPage
from test_pages.Terms_Of_Service_page import TermsOfServicePage


@pytest.mark.usefixtures("login")
class TestPrivacyAboutContact:

    def test_privacy_policy(self):
        privacy_page = PrivacyPolicyPage(self.driver)
        privacy_page.go_to_privacy_policy()

    def test_about_us(self):
        about_us_page = AboutUsPage(self.driver)
        about_us_page.go_to_about_us()

    def test_contact_us(self):
        contact_us_page = ContactUsPage(self.driver)
        contact_us_page.fill_contact_us_form("roronoa zoro", "roronoazoro3@gmail.com", "Hi! this is zoro")

    def test_terms_of_service(self):
        terms_page = TermsOfServicePage(self.driver)
        terms_page.go_to_terms_of_service()
