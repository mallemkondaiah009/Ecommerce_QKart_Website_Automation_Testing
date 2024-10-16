from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def logout(self):
        # Click on the Logout button
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Logout']").click()
        print("User has been logged out.")
