from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Login to QKart']")

    # Methods to interact with elements
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_submit(self):
        self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON).click()
