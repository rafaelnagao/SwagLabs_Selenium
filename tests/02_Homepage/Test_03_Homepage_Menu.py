import pytest
from pages.home_page import HomePage


@pytest.mark.usefixtures("logged_in_session")
@pytest.mark.homepage
@pytest.mark.e2e
class Test_03_Homepage_Menu:
    def test_open_menu(self):
        homepage = HomePage(self.driver)
        homepage.menu_open()
        assert homepage.is_menu_open() is True

    def test_close_menu(self):
        homepage = HomePage(self.driver)
        if homepage.is_menu_open():
            homepage.menu_close()
        assert homepage.is_menu_open() is False

    def test_click_outside_menu(self):
        homepage = HomePage(self.driver)
        homepage.menu_open()
        homepage.menu_outside_click()
        assert homepage.is_menu_open() is True
        homepage.menu_close()
    
    def test_menu_options(self):
        homepage = HomePage(self.driver)
        homepage.menu_open()
        options = homepage.get_menu_options()
        expected_options = ["All Items", "About", "Logout", "Reset App State"]
        assert options == expected_options
        homepage.menu_close()
    
    def test_menu_option_all_items(self):
        homepage = HomePage(self.driver)
        homepage.menu_open()
        homepage.click_menu_option("All Items")
        assert homepage.get_url() == "https://www.saucedemo.com/inventory.html"
        homepage.menu_close()

    def test_menu_option_about(self):
        homepage = HomePage(self.driver)
        homepage.menu_open()
        homepage.click_menu_option("About")
        assert "saucelabs.com" in homepage.get_url()
        self.driver.back()
    
    def test_menu_option_logout(self):
        homepage = HomePage(self.driver)
        homepage.menu_open()
        homepage.click_menu_option("Logout")
        assert homepage.get_url() == "https://www.saucedemo.com/"