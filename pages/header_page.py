import allure
from selenium.webdriver.common.by import By

from locators.patterns import A_CLS_CONTAINS, BUTTON, DIV_CLS_CONTAINS
from pages.base_page import BasePage


class HeaderPage(BasePage):
    ORDER_BTN = (
        By.XPATH, DIV_CLS_CONTAINS.format('Header') + BUTTON.format('Заказать'))
    SCOOTER_LOGO = By.XPATH, A_CLS_CONTAINS.format('Scooter')
    YANDEX_LOGO = By.XPATH, A_CLS_CONTAINS.format('Yandex')

    @allure.step('Клик по логотипу «Яндекс»')
    def yandex_logo_click(self):
        self.click_element(self.YANDEX_LOGO)

    @allure.step('Клик по логотипу «Самокат».')
    def scooter_logo_click(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step('Клик по кнопке «Заказать».')
    def order_button_click(self):
        self.click_element(self.ORDER_BTN)