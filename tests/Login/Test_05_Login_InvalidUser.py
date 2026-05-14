import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.e2e
class Test_05_Login_InvalidUser:

    def test_login_invalid_user(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("invalid_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Epic sadface: Username and password do not match any user in this service"