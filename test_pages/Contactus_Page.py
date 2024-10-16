from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_contact_us_form(self, name, email, message):
        # Fill the Contact Us form
        self.driver.find_element(By.XPATH, "//p[normalize-space()='Contact us']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Message']").send_keys(message)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Contact Now']").click()
        print(f"Contact Us form submitted with Name: {name}, Email: {email}, Message: {message}")
