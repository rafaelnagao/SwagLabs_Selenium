from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title = (By.CLASS_NAME, "inventory_details_name")
        self.product_description = (By.CLASS_NAME, "inventory_details_desc")
        self.product_price = (By.CLASS_NAME, "inventory_details_price")
        self.add_to_cart_button = (By.CLASS_NAME, "btn_primary")
        self.remove_button = (By.ID, "remove")
        self.back_to_products_button = (By.CLASS_NAME, "inventory_details_back_button")
        self.cart_badge_locator = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
    
    def go_to_product(self, product_name):
        product_link = (By.XPATH, f"//a[.//div[text()='{product_name}']]")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(product_link)
        ).click()

    def get_product_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.product_title)
        ).text.strip()
    
    def get_product_description(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.product_description)
        ).text.strip()
    
    def get_product_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.product_price)
        ).text.strip()
    
    def is_product_image_visible(self):
        image_locator = (By.CSS_SELECTOR, ".inventory_details_img_container img")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(image_locator)
            )
            return True
        except:
            return False
    
    def is_back_to_products_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.back_to_products_button)
            )
            return True
        except:
            return False

    def add_product_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        ).click()
    
    def remove_product_from_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.remove_button)
        ).click()
    
    def cart_item_count(self):
        badges = self.driver.find_elements(*self.cart_badge_locator)
        if not badges:
            return 0
        count_text = badges[0].text.strip()
        return int(count_text) if count_text.isdigit() else 0

    def go_back_to_products(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.back_to_products_button)
        ).click()
    
    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()