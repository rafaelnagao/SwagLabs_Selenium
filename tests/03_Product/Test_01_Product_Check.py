import pytest
from pages.product_page import ProductPage


@pytest.mark.usefixtures("logged_in_session")
@pytest.mark.product
@pytest.mark.e2e
class TestProductCheck:
    def test_product_details(self):
        product_page = ProductPage(self.driver)
        assert "inventory.html" in self.driver.current_url
        product_page.go_to_product("Sauce Labs Backpack")
        
        assert product_page.get_product_title() == "Sauce Labs Backpack"
        assert product_page.get_product_description() != ""
        assert product_page.get_product_price() == "$29.99"
        assert product_page.is_product_image_visible()
        assert product_page.is_back_to_products_visible()
    
    def test_cart_is_empty(self):
        product_page = ProductPage(self.driver)
        assert product_page.cart_item_count() == 0
    
    def test_back_to_products(self):
        product_page = ProductPage(self.driver)
        product_page.go_back_to_products()
        
        assert "inventory.html" in self.driver.current_url
    