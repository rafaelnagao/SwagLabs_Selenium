import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.e2e
class Test_03_Login_NoPassword:
    
    def test_login_no_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.click_login()

        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Epic sadface: Password is required"
