import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.e2e
class Test_07_Login_LockedOutUser:

    def test_login_locked_out_user(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("locked_out_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
    
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Epic sadface: Sorry, this user has been locked out."
