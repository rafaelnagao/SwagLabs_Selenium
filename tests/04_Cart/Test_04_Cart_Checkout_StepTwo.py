import pytest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("logged_in_session")
@pytest.mark.cart
@pytest.mark.e2e
class Test_04_Cart_Checkout_StepTwo:
    def test_checkout_step_two_process(self):
        homepage = HomePage(self.driver)
        cart_page = CartPage(self.driver)

        product_name = "Sauce Labs Backpack"
        homepage.add_product_to_cart(product_name)
        cart_page.go_to_cart()

        cart_page.click_checkout()

        cart_page.send_keys(By.ID, "first-name", "Rafael")
        cart_page.send_keys(By.ID, "last-name", "Nagao")
        cart_page.send_keys(By.ID, "postal-code", "12345")
        cart_page.click(By.ID, "continue")

        assert "checkout-step-two" in self.driver.current_url, "A URL não mudou para a página de checkout step two."
        assert cart_page.get_title() == "Checkout: Overview", "O título da página de checkout step two está incorreto."
        assert cart_page.is_product_in_cart(product_name) is True, f"O produto '{product_name}' não está presente na página de checkout step two."
        assert cart_page.get_cart_item_prices()[0] == "$29.99", f"O preço do produto '{product_name}' está incorreto na página de checkout step two."
        assert cart_page.get_cart_item_descriptions()[0] == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.", f"A descrição do produto '{product_name}' está incorreta na página de checkout step two."
        assert cart_page.cart_item_count() == 1, f"O número de itens no carrinho é diferente do esperado na página de checkout step two. Esperado: 1, Encontrado: {cart_page.cart_item_count()}"
        assert cart_page.get_cart_total() == "$32.39", f"O total do carrinho está incorreto na página de checkout step two. Esperado: '$32.39', Encontrado: '{cart_page.get_cart_total()}'"


    def test_checkout_step_two_cancel(self):
        cart_page = CartPage(self.driver)

        cancel_button = cart_page.is_element_present(By.ID, "cancel")
        assert cancel_button, "O botão 'Cancel' não está presente na página de checkout step two."
    
        cart_page.click(By.ID, "cancel")
        assert "inventory" in self.driver.current_url, "A URL não voltou para a página de inventário após cancelar o checkout."
    
    def test_checkout_step_two_finish(self):
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()

        cart_page.click_checkout()

        cart_page.send_keys(By.ID, "first-name", "Rafael")
        cart_page.send_keys(By.ID, "last-name", "Nagao")
        cart_page.send_keys(By.ID, "postal-code", "12345")
        cart_page.click(By.ID, "continue")

        screenshot_path = cart_page.take_full_page_screenshot("checkout_step_two.png")
        print(f"Screenshot salva em: {screenshot_path}")

        finish_button = cart_page.is_element_present(By.ID, "finish")
        assert finish_button, "O botão 'Finish' não está presente na página de checkout step two."
    
        cart_page.click(By.ID, "finish")
        assert "checkout-complete" in self.driver.current_url, "A URL não mudou para a página de checkout complete após finalizar o checkout."