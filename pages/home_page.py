from pathlib import Path

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.burger_menu_button = (By.ID, "react-burger-menu-btn")
        self.close_button = (By.ID, "react-burger-cross-btn")
        self.menu_options = (By.CLASS_NAME, "bm-item")
        self.body = (By.TAG_NAME, "body")
        self.social_media_twitter = (By.CSS_SELECTOR, "a[data-test='social-twitter']")
        self.social_media_facebook = (By.CSS_SELECTOR, "a[data-test='social-facebook']")
        self.social_media_linkedin = (By.CSS_SELECTOR, "a[data-test='social-linkedin']")

    def get_url(self):
        return self.driver.current_url

    def menu_open(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.burger_menu_button)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.close_button)
        )

    def menu_close(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_button)
        ).click()
        WebDriverWait(self.driver, 10).until_not(
            EC.visibility_of_element_located(self.close_button)
        )

    def is_menu_open(self):
        try:
            return WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(self.close_button)
            ).is_displayed()
        except TimeoutException:
            return False

    def get_menu_options(self):
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.menu_options)
        )
        return [option.text.strip() for option in options]

    def click_menu_option(self, option_text):
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.menu_options)
        )
        for option in options:
            if option.text.strip() == option_text:
                option.click()
                return
        raise Exception(f"Opção não encontrada: {option_text}")

    def menu_outside_click(self):
        self.driver.find_element(*self.body).click()

    def get_filter_options(self):
        filter_button = (By.CLASS_NAME, "product_sort_container")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(filter_button)
        ).click()
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product_sort_container option"))
        )
        return [option.text.strip() for option in options]
    
    def select_filter_option(self, option_text):
        filter_button = (By.CLASS_NAME, "product_sort_container")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(filter_button)
        ).click()
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product_sort_container option"))
        )
        for option in options:
            if option.text.strip() == option_text:
                option.click()
                return
        raise Exception(f"Opção de filtro não encontrada: {option_text}")
    
    def get_product_names(self):
        product_name_locator = (By.CLASS_NAME, "inventory_item_name")
        products = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(product_name_locator)
        )
        return [product.text.strip() for product in products]
    
    def get_product_prices(self):
        product_price_locator = (By.CLASS_NAME, "inventory_item_price")
        prices = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(product_price_locator)
        )
        return [price.text.strip() for price in prices]
    
    def get_product_descriptions(self):
        product_description_locator = (By.CLASS_NAME, "inventory_item_desc")
        descriptions = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(product_description_locator)
        )
        return [desc.text.strip() for desc in descriptions]
    
    def get_product_images(self):
        product_images_locator = (By.CSS_SELECTOR, ".inventory_item_img img")
        images = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(product_images_locator)
        )
        return [img.get_attribute("src") for img in images]
    
    def get_cart_count(self):
        cart_badge_locator = (By.CLASS_NAME, "shopping_cart_badge")
        try:
            cart_badge = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(cart_badge_locator)
            )
            return int(cart_badge.text.strip())
        except TimeoutException:
            return 0
        
    def add_product_to_cart(self, product_name):
        slug = product_name.lower().replace(" ", "-")
        product_id = f"add-to-cart-{slug}"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, product_id))
        ).click()

    def remove_product_from_cart(self, product_name):
        slug = product_name.lower().replace(" ", "-")
        product_id = f"remove-{slug}"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, product_id))
        ).click()

    def is_product_in_cart(self, product_name):
        slug = product_name.lower().replace(" ", "-")
        product_id = f"remove-{slug}"
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, product_id))
            )
            return button.is_displayed()
        except TimeoutException:
            return False
        
    def get_product_count(self):
        product_locator = (By.CLASS_NAME, "inventory_item")
        products = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(product_locator)
        )
        return len(products)
    
    def take_full_page_screenshot(self, file_name):
        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(parents=True, exist_ok=True)

        file_path = screenshots_dir / file_name
        success = self.driver.save_screenshot(str(file_path))

        assert success, f"Não foi possível salvar a screenshot em: {file_path}"
        return str(file_path)
    
    def get_twitter_urls(self):
        social_twitter = self.driver.find_elements(*self.social_media_twitter)
        return [link.get_attribute("href") for link in social_twitter]

    def get_facebook_urls(self):
        social_facebook = self.driver.find_elements(*self.social_media_facebook)
        return [link.get_attribute("href") for link in social_facebook]

    def get_linkedin_urls(self):
        social_linkedin = self.driver.find_elements(*self.social_media_linkedin)
        return [link.get_attribute("href") for link in social_linkedin]
    