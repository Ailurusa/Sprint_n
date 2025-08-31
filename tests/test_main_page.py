import allure
import pytest

from data import (
    FIRST_ADDRESS,
    SECOND_ADDRESS,
    DESCRIPTION_FOR_IDENTICAL_ADDRESSES,
    DURATION_FOR_IDENTICAL_ADDRESSES,
    TEXT_FROM_TAB_OPTIMAL,
    TEXT_FROM_TAB_FAST,
    TEXT_GET_TAXI_BUTTON,
    TEXT_GET_DRIVE_BUTTON,
)
from pages.main_page import MainPage


class TestMainPage:
    @allure.title("Отрисовка маршрута: на карте видны две точки (старт/финиш)")
    def test_enter_start_and_finish_travel_points_shows_points_on_the_map(self, driver):
        page = MainPage(driver)
        page.enter_from_address(FIRST_ADDRESS)
        page.enter_to_address(SECOND_ADDRESS)
        points_list = page.get_route_pins()
        assert len(points_list) == 2

    @allure.title("При вводе начальной и конечной точек появляется панель выбора маршрута")
    def test_enter_start_and_finish_travel_points_shows_choose_route_panel(self, driver):
        page = MainPage(driver)
        page.enter_from_address(SECOND_ADDRESS)
        page.enter_to_address(FIRST_ADDRESS)
        assert page.is_route_picker_visible()

    @allure.title("Одинаковые адреса → бесплатно и 0 минут в пути")
    def test_enter_identical_addresses_shows_text_count_free_time_zero(self, driver):
        page = MainPage(driver)
        page.enter_from_address(FIRST_ADDRESS)
        page.enter_to_address(FIRST_ADDRESS)
        assert page.is_route_picker_visible()
        assert (
                page.route_description_text() == DESCRIPTION_FOR_IDENTICAL_ADDRESSES
                and page.route_duration_text() == DURATION_FOR_IDENTICAL_ADDRESSES
        )

    @pytest.mark.parametrize(
        "switch_method, expected_tab_title",
        [
            (MainPage.click_tab_optimal, TEXT_FROM_TAB_OPTIMAL),
            (MainPage.click_tab_fast, TEXT_FROM_TAB_FAST),
        ],
    )
    @allure.title("Переключение тарифа на Оптимальный/Быстрый")
    def test_switch_to_optimal_or_fast_recalculates(self, driver_option_bike, switch_method, expected_tab_title):
        page = MainPage(driver_option_bike)
        old_duration = page.route_duration_text()
        old_description = page.route_description_text()
        switch_method(page)
        active_tab_text = page.active_tab_text()
        new_duration = page.route_duration_text()
        new_description = page.route_description_text()

        assert (
                active_tab_text == expected_tab_title
                and old_description != new_description
                and old_duration != new_duration
        )

    @allure.title("Переключение тарифа на «Свой» включает типы передвижения")
    def test_switch_to_self_enables_transport_options(self, driver_with_addresses):
        page = MainPage(driver_with_addresses)
        page.click_tab_fast()
        page.click_tab_custom()
        assert page.are_all_options_available()

    @allure.title("Быстрый маршрут показывает кнопку «Вызвать такси»")
    def test_fast_tab_shows_get_taxi_button(self, driver_with_addresses):
        page = MainPage(driver_with_addresses)
        page.click_tab_fast()
        assert page.result_button_text() == TEXT_GET_TAXI_BUTTON

    @allure.title("«Свой» + «Драйв» показывает кнопку «Забронировать»")
    def test_self_drive_shows_book_button(self, driver_with_addresses):
        page = MainPage(driver_with_addresses)
        page.click_tab_custom()
        page.select_option_drive()
        assert page.result_button_text() == TEXT_GET_DRIVE_BUTTON
