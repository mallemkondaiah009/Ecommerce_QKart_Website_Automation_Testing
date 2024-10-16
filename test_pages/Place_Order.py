from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_cart_and_checkout(self):
        # Wait for the 'Checkout' button to be visible and click it
        go_to_cart = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Checkout']"))
        )
        go_to_cart.click()

    def select_address(self):
        # Implicit wait before interacting with the address input
        self.driver.implicitly_wait(10)
        # Click on the address input field
        address_field = self.driver.find_element(By.XPATH, "//input[@name='address']")
        address_field.click()

    def place_order(self):
        # Click the 'PLACE ORDER' button
        place_order_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='PLACE ORDER']")
        place_order_button.click()

    def confirm_order(self):
        # Click the 'Continue' button to confirm the order
        continue_button = self.driver.find_element(By.XPATH, "//button[@id='continue-btn']")
        continue_button.click()
        print("Order placed successfully!")
