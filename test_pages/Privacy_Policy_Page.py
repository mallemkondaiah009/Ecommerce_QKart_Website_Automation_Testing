from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PrivacyPolicyPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_privacy_policy(self):
        # Click Privacy Policy link
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Privacy policy']").click()

        # Switch to the new window
        win = self.driver.window_handles
        self.driver.switch_to.window(win[0])
        print("Switched to Privacy Policy window.")
