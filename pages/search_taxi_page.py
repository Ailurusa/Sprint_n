import allure

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
        self.wait_text_in(L.HEADER_TIMER, {"00:01", "00:00"}, timeout=timeout, allow_missing=True)
        current = self._safe_text(L.HEADER_TIMER)
        if current == "00:01":
            self.wait_text_in(L.HEADER_TIMER, {"00:00"}, timeout=30, allow_missing=True)
