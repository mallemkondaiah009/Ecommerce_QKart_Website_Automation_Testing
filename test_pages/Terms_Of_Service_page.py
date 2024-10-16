from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TermsOfServicePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_terms_of_service(self):
        # Click Terms of Service link
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Terms of Service']").click()
        print("Navigated to Terms of Service page.")
