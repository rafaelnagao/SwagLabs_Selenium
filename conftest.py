import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def create_driver():
    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": False
    }

    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture
def setup_teardown(driver, request):
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver

@pytest.fixture
def logged_in_session(driver, request):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    request.cls.driver = driver