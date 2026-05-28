import pytest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("logged_in_session")
@pytest.mark.cart
@pytest.mark.e2e
class Test_03_Cart_Checkout:
    def test_checkout_step_one_fields(self):
        cart_page = CartPage(self.driver)
        homepage = HomePage(self.driver)

        homepage.add_product_to_cart("Sauce Labs Backpack")
        cart_page.go_to_cart()
        cart_page.click_checkout()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-one.html")
        )
        assert cart_page.is_element_present(By.ID, "first-name")
        assert cart_page.is_element_present(By.ID, "last-name")
        assert cart_page.is_element_present(By.ID, "postal-code")
    
    def test_checkout_step_one_fields_validation(self):
        cart_page = CartPage(self.driver)
        homepage = HomePage(self.driver)

        homepage.add_product_to_cart("Sauce Labs Backpack")
        cart_page.go_to_cart()
        cart_page.click_checkout()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-one.html")
        )

        cart_page.click(By.ID, "continue")

        error_message = cart_page.find_element(By.CLASS_NAME, "error-message-container").text.strip()
        assert error_message == "Error: First Name is required", f"A mensagem de erro para o campo 'First Name' está incorreta. Encontrada: '{error_message}'"

        cart_page.send_keys(By.ID, "first-name", "Rafael")
        cart_page.click(By.ID, "continue")

        error_message = cart_page.find_element(By.CLASS_NAME, "error-message-container").text.strip()
        assert error_message == "Error: Last Name is required", f"A mensagem de erro para o campo 'Last Name' está incorreta. Encontrada: '{error_message}'"

        cart_page.send_keys(By.ID, "last-name", "Nagao")
        cart_page.click(By.ID, "continue")

        error_message = cart_page.find_element(By.CLASS_NAME, "error-message-container").text.strip()
        assert error_message == "Error: Postal Code is required", f"A mensagem de erro para o campo 'Postal Code' está incorreta. Encontrada: '{error_message}'"

        cart_page.send_keys(By.ID, "postal-code", "12345")
        cart_page.click(By.ID, "continue")

    def test_checkout_step_one_cancel(self):
        cart_page = CartPage(self.driver)
        homepage = HomePage(self.driver)

        homepage.add_product_to_cart("Sauce Labs Backpack")
        cart_page.go_to_cart()
        cart_page.click_checkout()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-one.html")
        )

        cancel_button = cart_page.is_element_present(By.ID, "cancel")
        assert cancel_button, "O botão 'Cancel' não está presente na página de checkout."

        cart_page.click(By.ID, "cancel")

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("cart.html")
        )

        assert "cart.html" in self.driver.current_url, "A URL não voltou para a página do carrinho após cancelar o checkout."
    
    def test_checkout_step_one_continue(self):
        cart_page = CartPage(self.driver)
        homepage = HomePage(self.driver)
        homepage.add_product_to_cart("Sauce Labs Backpack")
        cart_page.go_to_cart()
        cart_page.click_checkout()

        cart_page.send_keys(By.ID, "first-name", "Rafael")
        cart_page.send_keys(By.ID, "last-name", "Nagao")
        cart_page.send_keys(By.ID, "postal-code", "12345")

        continue_button = cart_page.is_element_present(By.ID, "continue")
        assert continue_button, "O botão 'Continue' não está presente na página de checkout."

        cart_page.click(By.ID, "continue")

        assert "checkout-step-two" in self.driver.current_url, "A URL não mudou para a página de checkout step two após clicar em continuar."
    