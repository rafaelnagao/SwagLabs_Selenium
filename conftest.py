import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup_teardown(request):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")


    yield
    driver.quit()