import pytest
from pages.cart_page import CartPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("logged_in_session")
@pytest.mark.cart
@pytest.mark.e2e
class Test_02_Cart_Product:
    def test_add_product_to_cart(self):
        cart_page = CartPage(self.driver)
        homepage = HomePage(self.driver)

        product_name = "Sauce Labs Backpack"
        cart_page.go_to_cart_with_product(product_name)

        assert cart_page.is_product_in_cart(product_name) is True, f"O produto '{product_name}' não foi adicionado ao carrinho."

    def test_remove_product_from_cart(self):
        cart_page = CartPage(self.driver)

        product_name = "Sauce Labs Backpack"
        cart_page.remove_item(product_name)

        assert cart_page.is_product_in_cart(product_name) is False, f"O produto '{product_name}' não foi removido do carrinho."
    
    def test_cart_count_after_adding_products(self):
        homepage = HomePage(self.driver)
        cart_page = CartPage(self.driver)

        cart_page.continue_shopping()

        products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
        for product in products_to_add:
            homepage.add_product_to_cart(product)
        
        cart_page.go_to_cart()
        assert cart_page.cart_item_count() == len(products_to_add), f"O número de itens no carrinho é diferente do esperado. Esperado: {len(products_to_add)}, Encontrado: {cart_page.cart_item_count()}"
    
    def test_cart_count_after_removing_products(self):
        cart_page = CartPage(self.driver)

        products_to_remove = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
        for product in products_to_remove:
            cart_page.remove_item(product)
        
        assert cart_page.cart_item_count() == 0, f"O carrinho não está vazio após remover os produtos. Itens restantes: {cart_page.cart_item_count()}"