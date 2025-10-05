import allure
from selenium.webdriver.common.by import By

from locators.patterns import BUTTON, DIV_CLS_CONTAINS
from pages.base_page import BasePage


class MainPage(BasePage):
    ANSWER = By.XPATH, '//div[@id="accordion__panel-{}"]/p'
    QUESTION = By.ID, 'accordion__heading-{}'
    ORDER_BTN = (
        By.XPATH,
        DIV_CLS_CONTAINS.format('FinishButton') + BUTTON.format('Заказать')
    )

    def format_locator(self, num, locator):
        method, pattern = locator
        return method, pattern.format(num)

    @allure.step('Клик по кнопке «Заказать».')
    def order_button_click(self):
        self.scroll_to_element(self.ORDER_BTN)
        self.click_element(self.ORDER_BTN)

    @allure.step('Получение текста кнопки-вопроса.')
    def get_question_text(self, num):
        return self.get_element(self.format_locator(num, self.QUESTION)).text

    @allure.step('Клик по кнопке-вопросу.')
    def question_click(self, num):
        self.scroll_to_element(self.format_locator(num, self.QUESTION))
        self.click_element(self.format_locator(num, self.QUESTION))

    @allure.step('Получение текста ответа на вопрос.')
    def get_answer_text(self, num):
        return self.get_element(self.format_locator(num, self.ANSWER)).text

    @allure.step('Проверка отображения ответа на вопрос.')
    def check_answer_field_is_shown(self, num):
        return self.get_element(
            self.format_locator(num, self.ANSWER)
        ).is_displayed()

    @allure.step('Ожидание появления ответа на вопрос {num}')
    def wait_for_answer_to_appear(self, num, timeout=5):
        answer_locator = self.format_locator(num, self.ANSWER)
        return self.wait_for_element_visible(answer_locator, timeout=timeout)