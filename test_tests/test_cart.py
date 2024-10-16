import pytest
from test_pages.cart_page import CartPage

@pytest.mark.usefixtures("login")  # Automatically login before this test
class TestQKartAddToCart:

    def test_add_to_cart(self):
        # Initialize CartPage object
        cart_page = CartPage(self.driver)

        # Add the first product to the cart
        cart_page.add_product1_to_cart()

        # Add the second product to the cart
        cart_page.add_product2_to_cart()

