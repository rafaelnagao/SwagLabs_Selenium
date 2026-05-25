import pytest
from pages.home_page import HomePage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("logged_in_session")
@pytest.mark.homepage
@pytest.mark.e2e
class Test_01_Homepage:
    def test_homepage_title(self):
        homepage = HomePage(self.driver)
        title = homepage.get_title()
        assert title == "Swag Labs"

    def test_homepage_url(self):
        homepage = HomePage(self.driver)
        url = homepage.get_url()
        assert url == "https://www.saucedemo.com/inventory.html"
    
    def test_check_filter_options(self):
        homepage = HomePage(self.driver)
        options = homepage.get_filter_options()
        expected_options = [
            "Name (A to Z)",
            "Name (Z to A)",
            "Price (low to high)",
            "Price (high to low)"
        ]
        assert options == expected_options
    
    def test_check_cart_icon(self):
        homepage = HomePage(self.driver)
        try:
            cart_icon = homepage.wait.until(lambda d: d.find_element(By.CLASS_NAME, "shopping_cart_link"))
            assert cart_icon.is_displayed()
        except:
            pytest.fail("Cart icon not found")

    def test_product_count(self):
        homepage = HomePage(self.driver)
        count = homepage.get_product_count()
        assert count == 6
    
    def test_product_names(self):
        homepage = HomePage(self.driver)
        names = homepage.get_product_names()
        expected_names = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)"
        ]
        assert names == expected_names
    
    def test_product_prices(self):
        homepage = HomePage(self.driver)
        prices = homepage.get_product_prices()
        expected_prices = [
            "$29.99",
            "$9.99",
            "$15.99",
            "$49.99",
            "$7.99",
            "$15.99"
        ]
        assert prices == expected_prices
    
    def test_product_descriptions(self):
        homepage = HomePage(self.driver)
        descriptions = homepage.get_product_descriptions()
        expected_descriptions = [
            "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
            "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
            "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.",
            "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
            "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
            "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton."
        ]
        assert descriptions == expected_descriptions
    
    def test_product_images(self):
        homepage = HomePage(self.driver)
        images = homepage.get_product_images()

        assert len(images) == 6
        assert all(img is not None for img in images)
        assert all(img.startswith("https://www.saucedemo.com/static/media/") for img in images)
        
        screenshot_path = homepage.take_full_page_screenshot("homepage_products.png")
        print(f"Screenshot salva em: {screenshot_path}")
