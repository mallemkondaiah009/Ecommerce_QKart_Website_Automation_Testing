import pytest
from test_pages.Place_Order import OrderPage
from test_pages.cart_page import CartPage
@pytest.mark.usefixtures("login")
class TestOrderPage:

    def test_order_from_cart(self, init_driver):

        cart_page = CartPage(self.driver)  # Assuming CartPage contains methods for adding products
        cart_page.add_product1_to_cart()  # Add product 1 to cart
        cart_page.add_product2_to_cart()

        # Step 1: Go to the cart and proceed to checkout
        order_page = OrderPage(init_driver)
        order_page.go_to_cart_and_checkout()

        # Step 2: Select the address by clicking the address input field
        order_page.select_address()

        # Step 3: Place the order
        order_page.place_order()

        # Step 4: Confirm the order
        order_page.confirm_order()
