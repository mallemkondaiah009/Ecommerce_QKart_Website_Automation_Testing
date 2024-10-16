from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Register']")
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "confirmPassword")
    REGISTER_NOW_BUTTON = (By.XPATH, "//button[normalize-space()='Register Now']")

    # Methods to interact with elements
    def click_register(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.CONFIRM_PASSWORD_FIELD).send_keys(confirm_password)

    def click_register_now(self):
        self.driver.find_element(*self.REGISTER_NOW_BUTTON).click()
