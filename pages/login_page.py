from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")
        
    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.username_input))
        field.clear()
        field.send_keys(username)
    
    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.password_input))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
    
    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.error_message)
        ).text

    def error_message_displayed(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.error_message)
            ).is_displayed()
        except:
            return False