from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with


class SearchBar:
    def __init__(self, driver):
        self.driver = driver

    # Locator for Logout Button
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='primary']")

    # Method to perform search
    def search_item(self, search_term):
        # Wait until the logout button is visible
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOGOUT_BUTTON)
        )

        # Find the input field located to the left of the logout button
        input_field = self.driver.find_element(
            locate_with(By.TAG_NAME, "input").to_left_of(logout_button)
        )

        # Enter search term into the input field
        input_field.send_keys(search_term)

        # Find the SVG search button to the left of the logout button and click it
        svg_field = self.driver.find_element(
            locate_with(By.TAG_NAME, "svg").to_left_of(logout_button)
        )
        svg_field.click()
