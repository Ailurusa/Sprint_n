import allure

from data import (
    SEARCH_TAXI_TITLE_TEXT,
    SEARCH_TAXI_DETAILS_BUTTON_TEXT,
    SEARCH_TAXI_RETURN_BUTTON_TEXT,
    FINISH_ORDER_TAXI_TITLE_RE,
)
from pages.get_taxi_page import GetTaxiPage
from pages.search_taxi_page import SearchTaxiPage


class TestSearchTaxi:
    @allure.title("Нажатие «Ввести номер и заказать» открывает окно ожидания машины")
    def test_click_on_extra_info_get_taxi_button_open_waiting_taxi_window(self, driver_open_choose_taxi_panel):
        get_taxi_panel = GetTaxiPage(driver_open_choose_taxi_panel)
        get_taxi_panel.click_on_work_tariff()
        get_taxi_panel.click_on_extra_wishes_title()
        get_taxi_panel.scroll_down_extra_panel()
        get_taxi_panel.click_on_extra_wishes_laptop_checkbox()
        get_taxi_panel.click_on_extra_info_get_taxi_button()
        search_taxi_panel = SearchTaxiPage(driver_open_choose_taxi_panel)
        assert search_taxi_panel.title_text() == SEARCH_TAXI_TITLE_TEXT

    @allure.title("Элементы окна ожидания машины соответствуют ТЗ")
    def test_search_taxi_panel_elements_visible_and_has_expected_texts(self, driver_open_search_taxi_panel):
        page = SearchTaxiPage(driver_open_search_taxi_panel)
        assert (
                page.title_text() == SEARCH_TAXI_TITLE_TEXT
                and page.timer_is_visible()
                and page.cancel_label() == SEARCH_TAXI_RETURN_BUTTON_TEXT
                and page.details_label() == SEARCH_TAXI_DETAILS_BUTTON_TEXT
        )

    @allure.title("После окончания таймера отображается окно завершённого заказа")
    def test_timer_end_open_order_window(self, driver_open_search_taxi_panel):
        page = SearchTaxiPage(driver_open_search_taxi_panel)
        page.wait_timer_finish()
        title_after_timer = page.title_text()
        assert FINISH_ORDER_TAXI_TITLE_RE in title_after_timer
