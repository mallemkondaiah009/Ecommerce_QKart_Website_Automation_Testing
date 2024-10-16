from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AboutUsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_about_us(self):
        # Click About Us link
        self.driver.find_element(By.XPATH, "//a[normalize-space()='About us']").click()

        # Switch to the new window
        win = self.driver.window_handles
        self.driver.switch_to.window(win[0])
        print("Switched to About Us window.")
