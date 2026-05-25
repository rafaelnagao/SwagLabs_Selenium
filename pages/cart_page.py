from pathlib import Path
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.title = (By.CLASS_NAME, "title")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.cancel_button = (By.ID, "cancel")
        self.finish_button = (By.ID, "finish")
        self.error_message_container = (By.CLASS_NAME, "error-message-container")
        self.cart_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_item_price = (By.CLASS_NAME, "inventory_item_price")
        self.cart_item_desc = (By.CLASS_NAME, "inventory_item_desc")
        self.cart_item_name_locator = (By.CLASS_NAME, "inventory_item_name")
        self.cart_item_price_locator = (By.CLASS_NAME, "inventory_item_price")
        self.cart_item_desc_locator = (By.CLASS_NAME, "inventory_item_desc")
        self.cart_total_locator = (By.CLASS_NAME, "summary_total_label")


    def go_to_cart(self):
        self.click(*self.cart_link)

    def get_title(self):
        return self.find_element(*self.title).text.strip()

    def get_cart_items(self):
        return self.find_elements(*self.cart_items)
    
    def is_element_present(self, by, value):
        try:
            self.find_element(by, value)
            return True
        except:
            return False
    
    def click(self, by, value):
        self.find_element(by, value).click()
    
    def send_keys(self, by, value, keys):
        self.find_element(by, value).send_keys(keys)
    
    def find_element(self, by, value):
        return self.driver.find_element(by, value)
    
    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def click_checkout(self):
        self.click(*self.checkout_button)

    def continue_shopping(self):
        self.click(*self.continue_shopping_button)

    def is_product_in_cart(self, product_name):
        for item in self.get_cart_items():
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            if name == product_name:
                return True
        return False

    def remove_item(self, product_name):
        for item in self.get_cart_items():
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            if name == product_name:
                item.find_element(By.TAG_NAME, "button").click()
                return
        raise ValueError(f"Produto '{product_name}' não encontrado no carrinho.")

    def cart_item_count(self):
        return len(self.get_cart_items())
    
    def ensure_cart_is_empty(self):
        while self.cart_item_count() > 0:
            first_item = self.get_cart_items()[0]
            product_name = first_item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            self.remove_item(product_name)
    
    def first_name_required_error(self):
        return self.find_element(*self.error_message_container).text.strip() == "Error: First Name is required"
    
    def last_name_required_error(self):
        return self.find_element(*self.error_message_container).text.strip() == "Error: Last Name is required"
    
    def postal_code_required_error(self):
        return self.find_element(*self.error_message_container).text.strip() == "Error: Postal Code is required"
    
    def is_checkout_button_present(self):
        return self.is_element_present(*self.checkout_button)
    
    def is_continue_shopping_button_present(self):
        return self.is_element_present(*self.continue_shopping_button)
    
    def is_cancel_button_present(self):
        return self.is_element_present(*self.cancel_button)
    
    def is_finish_button_present(self):
        return self.is_element_present(*self.finish_button)
    
    def get_cart_item_names(self):
        return [item.find_element(*self.cart_item_name_locator).text.strip() for item in self.get_cart_items()]
    
    def get_cart_item_prices(self):
        return [item.find_element(*self.cart_item_price_locator).text.strip() for item in self.get_cart_items()]
    
    def get_cart_item_descriptions(self):
        return [item.find_element(*self.cart_item_desc_locator).text.strip() for item in self.get_cart_items()]
    
    def get_cart_total(self):
        total_element = self.find_element(*self.cart_total_locator)
        total_text = total_element.text.strip()
        return total_text.replace("Total: ", "")

    def take_full_page_screenshot(self, file_name):
        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(parents=True, exist_ok=True)

        file_path = screenshots_dir / file_name
        success = self.driver.save_screenshot(str(file_path))

        assert success, f"Não foi possível salvar a screenshot em: {file_path}"
        return str(file_path)