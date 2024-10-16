from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators for the products' "Add to Cart" buttons
    PRODUCT_1_BUTTON = (By.XPATH, "//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-9 product-grid css-14gqd74']//div[1]//div[1]//div[2]//button[1]")
    PRODUCT_2_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/button[1]")

    # Method to add the first product to the cart
    def add_product1_to_cart(self):
        product1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_1_BUTTON)
        )
        product1.click()

    # Method to add the second product to the cart
    def add_product2_to_cart(self):
        product2 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_2_BUTTON)
        )
        product2.click()
