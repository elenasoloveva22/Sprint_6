from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait

WAIT_SECONDS = 5


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.get_element(locator).click()

    def wait_for(self, event, seconds=WAIT_SECONDS):
        WebDriverWait(self.driver, seconds).until(event)

    def switch_window(self, url):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_for(e_c.url_to_be(url))

    def scroll_to_element(self, locator):
        self.driver.execute_script(
            'arguments[0].scrollIntoView()', self.get_element(locator)
        )
        self.wait_for(e_c.visibility_of_element_located(locator))

    def fill_form_field(self, locator, *value):
        self.get_element(locator).send_keys(value)