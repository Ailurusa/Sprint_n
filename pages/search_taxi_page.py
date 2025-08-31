import allure
from selenium.webdriver.support.ui import WebDriverWait

from locators.taxi_search_locators import TaxiSearchLocators as L
from pages.base_page import BasePage


class SearchTaxiPage(BasePage):

    @allure.step("Заголовок окна поиска такси")
    def title_text(self) -> str:
        self.wait_for_visibility(L.HEADER_TITLE)
        return self.extract_text(L.HEADER_TITLE)

    @allure.step("Текст кнопки «Отменить»")
    def cancel_label(self) -> str:
        self.wait_for_visibility(L.CANCEL_BUTTON_LABEL)
        return self.extract_text(L.CANCEL_BUTTON_LABEL)

    @allure.step("Текст кнопки «Детали»")
    def details_label(self) -> str:
        self.wait_for_visibility(L.DETAILS_BUTTON_LABEL)
        return self.extract_text(L.DETAILS_BUTTON_LABEL)

    @allure.step("Таймер отображается")
    def timer_is_visible(self) -> bool:
        try:
            self.wait_for_visibility(L.HEADER_TIMER)
            return True
        except TimeoutError:
            return False

    @allure.step("Дождаться окончания таймера")
    def wait_timer_finish(self, timeout: int = 60):
        def current_timer_text():
            try:
                return self.extract_text(L.HEADER_TIMER).strip()
            except Exception:
                return None

        WebDriverWait(self.browser, timeout).until(
            lambda d: (t := current_timer_text()) in {"00:01", "00:00", None}
        )

        if current_timer_text() == "00:01":
            WebDriverWait(self.browser, 30).until(
                lambda d: (t := current_timer_text()) in {"00:00", None}
            )
