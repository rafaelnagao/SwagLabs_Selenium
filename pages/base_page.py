import base64
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action_chains = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def get_title(self):
        return self.driver.title

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

    def take_full_page_screenshot(self, file_name):
        screenshot_dir = os.path.join(os.getcwd(), "tests", "Homepage", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, file_name)

        metrics = self.driver.execute_cdp_cmd("Page.getLayoutMetrics", {})
        content_size = metrics["contentSize"]

        screenshot = self.driver.execute_cdp_cmd(
            "Page.captureScreenshot",
            {
                "fromSurface": True,
                "captureBeyondViewport": True,
                "clip": {
                    "x": 0,
                    "y": 0,
                    "width": content_size["width"],
                    "height": content_size["height"],
                    "scale": 1
                }
            }
        )

        with open(screenshot_path, "wb") as file:
            file.write(base64.b64decode(screenshot["data"]))

        return screenshot_path
    
    def click_browser_back(self):
        self.driver.back()
    