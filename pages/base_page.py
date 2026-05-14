from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action_chains = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element with locator {locator} not found within the timeout period.")

    def find_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_elements(*locator)

    def send_keys(self, locator, text):
        self.wait_for_element(locator)
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        self.wait_for_element(locator)
        element = self.find_element(locator)
        element.click()

    def element_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False
    
    def element_exists(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def element_not_exists(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return False
        except TimeoutException:
            return True
