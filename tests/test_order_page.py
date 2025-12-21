import allure
import pytest

from data import BOOKED, SCENARIO_1, SCENARIO_2
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Создание заказа')
    @pytest.mark.parametrize(
        'scenario',
        [pytest.param(SCENARIO_1, id='Header button'),
         pytest.param(SCENARIO_2, id='Main button')]
    )
    def test_create_order_with_button_header_or_main(self, driver, scenario):
        page_obj, customer, rent = scenario
        page_obj(driver).order_button_click()
        order_page = OrderPage(driver)
        order_page.create_order(customer, rent)
        assert BOOKED in order_page.get_order_confirmed_title()