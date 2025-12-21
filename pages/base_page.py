import allure
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait

WAIT_SECONDS = 5


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Найти элемент по локатору {locator}')
    def get_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на элемент по локатору {locator}')
    def click_element(self, locator):
        self.get_element(locator).click()

    @allure.step('Ожидание события в течение {seconds} секунд')
    def wait_for(self, event, seconds=WAIT_SECONDS):
        WebDriverWait(self.driver, seconds).until(event)

    @allure.step('Ожидание условия в течение {timeout} секунд')
    def wait_for_condition(self, condition, timeout=WAIT_SECONDS, message=""):
        return WebDriverWait(self.driver, timeout).until(condition, message=message)

    @allure.step('Ожидание видимости элемента в течение {timeout} секунд')
    def wait_for_element_visible(self, locator, timeout=WAIT_SECONDS):
        return self.wait_for_condition(
            e_c.visibility_of_element_located(locator),
            timeout=timeout,
            message=f"Элемент не стал видимым за {timeout} секунд")

    @allure.step('Ожидание кликабельности элемента в течение {timeout} секунд')
    def wait_for_element_clickable(self, locator, timeout=WAIT_SECONDS):
        return self.wait_for_condition(
            e_c.element_to_be_clickable(locator),
            timeout=timeout,
            message=f"Элемент не стал кликабельным за {timeout} секунд")

    @allure.step('Переключиться на новую вкладку с URL: {url}')
    def switch_window(self, url):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_for(e_c.url_to_be(url))

    @allure.step('Проскроллить к элементу')
    def scroll_to_element(self, locator):
        self.driver.execute_script(
            'arguments[0].scrollIntoView()', self.get_element(locator))
        self.wait_for_element_visible(locator)

    @allure.step('Заполнить поле {locator}')
    def fill_form_field(self, locator, *values):
        element = self.get_element(locator)
        element.send_keys(*values)