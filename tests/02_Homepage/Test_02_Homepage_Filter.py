import pytest
from pages.home_page import HomePage


@pytest.mark.usefixtures("logged_in_session")
@pytest.mark.homepage
@pytest.mark.e2e
class Test_02_Homepage_Filter:
    def test_filter_a_to_z(self):
        homepage = HomePage(self.driver)
        homepage.select_filter_option("Name (A to Z)")
        names = homepage.get_product_names()
        expected_names = sorted(names)
        assert names == expected_names

    def test_filter_z_to_a(self):
        homepage = HomePage(self.driver)
        homepage.select_filter_option("Name (Z to A)")
        names = homepage.get_product_names()
        expected_names = sorted(names, reverse=True)
        assert names == expected_names

    def test_filter_low_to_high(self):
        homepage = HomePage(self.driver)
        homepage.select_filter_option("Price (low to high)")
        prices = homepage.get_product_prices()
        expected_prices = sorted(prices, key=lambda x: float(x.replace("$", "")))
        assert prices == expected_prices

    def test_filter_high_to_low(self):
        homepage = HomePage(self.driver)
        homepage.select_filter_option("Price (high to low)")
        prices = homepage.get_product_prices()
        expected_prices = sorted(prices, key=lambda x: float(x.replace("$", "")), reverse=True)
        assert prices == expected_prices
    