import pytest
from pages.product_page import ProductPage


@pytest.mark.usefixtures("logged_in_session")
@pytest.mark.product
@pytest.mark.e2e
class TestProductAddToCart:
    def test_add_to_cart(self):
        product_page = ProductPage(self.driver)
        product_page.go_to_product("Sauce Labs Backpack")
        assert "inventory-item.html?id=4" in self.driver.current_url
        
        product_page.add_product_to_cart()
        assert product_page.cart_item_count() == 1
    
    def test_remove_from_cart(self):
        product_page = ProductPage(self.driver)
        assert "inventory-item.html?id=4" in self.driver.current_url
        
        product_page.remove_product_from_cart()
        assert product_page.cart_item_count() == 0

    def test_cart_persistence(self):
        product_page = ProductPage(self.driver)
        assert "inventory-item.html?id=4" in self.driver.current_url
        
        product_page.add_product_to_cart()
        assert product_page.cart_item_count() == 1

        self.driver.refresh()
        assert product_page.cart_item_count() == 1
    
    def test_cart_navigation(self):
        product_page = ProductPage(self.driver)
        assert "inventory-item.html?id=4" in self.driver.current_url
        assert product_page.cart_item_count() == 1

        product_page.go_to_cart()
        assert "cart.html" in self.driver.current_url