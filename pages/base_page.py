import allure
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Ждем, пока элемент станет видимым')
    def wait_for_visibility(self, locator):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Клик по элементу')
    def tap(self, locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step('Ввод текста в поле')
    def fill_field(self, locator, text):
        field = self.browser.find_element(*locator)
        field.clear()
        field.send_keys(text)

    @allure.step('Получение текста элемента')
    def extract_text(self, locator):
        return self.browser.find_element(*locator).text

    @allure.step('Проверка, что элемент отображается')
    def is_visible(self, locator):
        try:
            return self.browser.find_element(*locator).is_displayed()
        except Exception:
            return False

    @allure.step('Проверка, что элемент не отображается')
    def is_invisible(self, locator):
        try:
            WebDriverWait(self.browser, 10).until(EC.invisibility_of_element(locator))
            return True
        except TimeoutError:
            return False

    @allure.step('Поиск одного элемента')
    def get_element(self, locator):
        method, value = locator
        return self.browser.find_element(method, value)

    @allure.step("Наводим фокус на элемент")
    def focus_on_element(self, locator):
        self.wait_for_visibility(locator)
        element = self.get_element(locator)
        ActionChains(self.browser).move_to_element(element).perform()

    @allure.step("Скроллим до конца")
    def move_to_down_in_container(self, container_locator):
        self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", container_locator)

    def _safe_text(self, locator):
        try:
            return self.extract_text(locator).strip()
        except (StaleElementReferenceException, NoSuchElementException):
            return None

    @allure.step("Ждем, пока текст элемента станет одним из ожидаемых значений")
    def wait_text_in(self, locator, expected_values, timeout=30, allow_missing=False):
        expected = set(expected_values)

        def cond(_):
            t = self._safe_text(locator)
            if t is None:
                return allow_missing
            return t in expected

        WebDriverWait(self.browser, timeout).until(cond)
