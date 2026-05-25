import pytest
from pages.cart_page import CartPage


@pytest.mark.usefixtures("logged_in_session")
@pytest.mark.cart
@pytest.mark.e2e
class Test_01_Cart_Check:
    def test_check_cart_is_empty(self):
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        cart_page.ensure_cart_is_empty()

        assert cart_page.cart_item_count() == 0, "O carrinho não está vazio."
    
    def test_check_title_cart_page(self):
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        assert cart_page.get_title() == "Your Cart", "O título da página do carrinho está incorreto."
    
    def test_check_checkout_button_presence(self):
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        assert cart_page.is_element_present(*cart_page.checkout_button), "O botão de checkout não está presente na página do carrinho."
    
    def test_check_continue_shopping_button_presence(self):
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        assert cart_page.is_element_present(*cart_page.continue_shopping_button), "O botão de continuar comprando não está presente na página do carrinho."
    