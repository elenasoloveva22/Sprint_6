import allure
import pytest
from data import FAQ
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Корректное отображение ответа на вопрос')
    @pytest.mark.parametrize('num', list(FAQ.keys()))
    def test_click_on_question_shows_answer(self, driver, num):
        main_page = MainPage(driver)
        
        # Проверяем вопрос
        assert main_page.get_question_text(num) == FAQ[num]['q']
        
        # Проверяем что ответ скрыт
        assert not main_page.check_answer_field_is_shown(num)
        
        # Кликаем на вопрос
        main_page.question_click(num)
        
        # Ждем появления ответа через метод страницы
        main_page.wait_for_answer_to_appear(num, timeout=5)
        
        # Проверяем ответ
        assert main_page.check_answer_field_is_shown(num)
        assert main_page.get_answer_text(num) == FAQ[num]['a']