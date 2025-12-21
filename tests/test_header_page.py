import allure
import pytest

from urls import MAIN_PAGE, ORDER_PAGE, REDIRECT
from pages.header_page import HeaderPage


class TestHeaderPage:
    @allure.title('Редирект по клику на лого «Яндекс» и «Самокат»')
    @pytest.mark.parametrize(
        'name, url',
        [pytest.param('yandex', REDIRECT, id='Logo Yandex'),
         pytest.param('scooter', MAIN_PAGE, id='Logo Scooter')]
    )
    def test_logo_click_redirect(self, driver, name, url):
        header_page = HeaderPage(driver)
        header_page.order_button_click()
        assert header_page.get_current_url() == ORDER_PAGE
        getattr(header_page, f'{name}_logo_click')()
        header_page.switch_window(url)
        assert header_page.get_current_url() == url