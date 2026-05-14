import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.e2e
class Test_01_Login_HappyPath:

    def test_login_happy_path(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert self.driver.find_element(By.CLASS_NAME, "inventory_list").is_displayed()