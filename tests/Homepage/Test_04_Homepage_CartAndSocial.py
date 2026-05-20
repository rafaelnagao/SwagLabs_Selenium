import pytest
from pages.home_page import HomePage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("logged_in_session")
@pytest.mark.homepage
@pytest.mark.e2e
class Test_04_Homepage_CartAndSocial:
    def test_cart_icon(self):
        homepage = HomePage(self.driver)
        cart_icon = homepage.find_element((By.CLASS_NAME, "shopping_cart_link"))
        assert cart_icon.is_displayed()
    
    def test_cart_count_initial(self):
        homepage = HomePage(self.driver)
        cart_count = homepage.get_cart_count()
        assert cart_count == 0
    
    def test_add_product_to_cart(self):
        homepage = HomePage(self.driver)
        product_name = "Sauce Labs Backpack"
        homepage.add_product_to_cart(product_name)
        assert homepage.is_product_in_cart(product_name) is True
        cart_count = homepage.get_cart_count()
        assert cart_count == 1
    
    def test_remove_product_from_cart(self):
        homepage = HomePage(self.driver)
        product_name = "Sauce Labs Backpack"
        homepage.remove_product_from_cart(product_name)
        assert homepage.is_product_in_cart(product_name) is False
        cart_count = homepage.get_cart_count()
        assert cart_count == 0
    
    def test_cart_count_multiple_products(self):
        homepage = HomePage(self.driver)
        products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
        for product in products_to_add:
            homepage.add_product_to_cart(product)
        cart_count = homepage.get_cart_count()
        assert cart_count == len(products_to_add)
        for product in products_to_add:
            homepage.remove_product_from_cart(product)
        cart_count = homepage.get_cart_count()
        assert cart_count == 0

    def test_social_links(self):
        homepage = HomePage(self.driver)
        twitter_link = homepage.find_element((By.CLASS_NAME, "social_twitter"))
        facebook_link = homepage.find_element((By.CLASS_NAME, "social_facebook"))
        linkedin_link = homepage.find_element((By.CLASS_NAME, "social_linkedin"))
        assert twitter_link.is_displayed()
        assert facebook_link.is_displayed()
        assert linkedin_link.is_displayed()

    def test_social_links_urls(self):
        homepage = HomePage(self.driver)
        twitter_urls = homepage.get_twitter_urls()
        facebook_urls = homepage.get_facebook_urls()
        linkedin_urls = homepage.get_linkedin_urls()

        assert twitter_urls == ["https://twitter.com/saucelabs"]
        assert facebook_urls == ["https://www.facebook.com/saucelabs"]
        assert linkedin_urls == ["https://www.linkedin.com/company/sauce-labs/"]
        