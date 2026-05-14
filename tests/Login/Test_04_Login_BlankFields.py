import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.e2e
class Test_04_Login_BlankFields:
    
    def test_login_blank_fields(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login()

        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Epic sadface: Username is required"
