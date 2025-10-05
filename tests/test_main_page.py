import allure
import pytest

import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import FAQ
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Корректное отображение ответа на вопрос')
    @pytest.mark.parametrize('num', FAQ)
    def test_click_on_question_shows_answer(self, driver, num):
        main_page = MainPage(driver)
        
        # Проверяем вопрос
        assert main_page.get_question_text(num) == FAQ[num]['q']
        
        # Проверяем что ответ скрыт
        assert not main_page.check_answer_field_is_shown(num)
        
        # Кликаем на вопрос
        main_page.question_click(num)
        
        # Ждем появления ответа с таймаутом
        wait = WebDriverWait(driver, 5)
        wait.until(lambda d: main_page.check_answer_field_is_shown(num))
        
        # Проверяем ответ
        assert main_page.check_answer_field_is_shown(num)
        assert main_page.get_answer_text(num) == FAQ[num]['a']