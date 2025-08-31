import allure
import pytest

from data import (
    TARIFFS_INFO,
    EXTRA_INFO_PHONE_FIELD_TEXT,
    EXTRA_INFO_PAYMENT_INFO_TEXT,
    EXTRA_INFO_COMMENT_FIELD_TEXT,
    EXTRA_INFO_EXTRA_WISHES_TEXT,
    EXTRA_INFO_GET_TAXI_BUTTON_TEXT,
)
from pages.get_taxi_page import GetTaxiPage


class TestGetTaxi:
    @allure.title("Открывается форма заказа со всеми 6 тарифами по ТЗ")
    def test_actual_list_of_tariffs_identical_with_expected_tariffs_list(self, driver_open_choose_taxi_panel):
        page = GetTaxiPage(driver_open_choose_taxi_panel)
        assert page.is_all_expected_tariffs_in_tariffs_names_list() and page.is_all_visible_tariffs_is_expected()

    @allure.title("В списке тарифов по умолчанию один тариф — активный")
    def test_tariffs_list_include_active_tariff(self, driver_open_choose_taxi_panel):
        page = GetTaxiPage(driver_open_choose_taxi_panel)
        assert page.is_active_tariff_in_tariff_names_list()

    @allure.title("При наведении на «i» отображается подсказка с информацией о тарифе")
    def test_focus_on_info_button_shows_info_panel(self, driver_open_choose_taxi_panel):
        page = GetTaxiPage(driver_open_choose_taxi_panel)
        page.focus_on_info_icon()
        assert page.is_info_panel_visible()

    @allure.title("Карточка «i»: заголовок и описание соответствуют ТЗ (параметризация)")
    @pytest.mark.xfail(reason="описания для тарифов «Сонный» и «Разговорчивый» перепутаны на стенде")
    @pytest.mark.parametrize(
        "click_method, tariff_name",
        [
            (GetTaxiPage.click_on_work_tariff, "Рабочий"),
            (GetTaxiPage.click_on_sleep_tariff, "Сонный"),
            (GetTaxiPage.click_on_holiday_tariff, "Отпускной"),
            (GetTaxiPage.click_on_talk_tariff, "Разговорчивый"),
            (GetTaxiPage.click_on_glad_tariff, "Утешительный"),
            (GetTaxiPage.click_on_glam_tariff, "Глянцевый"),
        ],
    )
    def test_info_panel_title_and_description_match_with_expected_texts(
            self, driver_open_choose_taxi_panel, click_method, tariff_name
    ):
        page = GetTaxiPage(driver_open_choose_taxi_panel)
        click_method(page)
        page.focus_on_info_icon()
        actual_title = page.get_info_panel_title()
        actual_description = page.get_info_panel_description()
        expected = TARIFFS_INFO[tariff_name]
        assert actual_title == expected["title"] and actual_description == expected["description"]

    @allure.title("Блок доп. информации содержит нужные поля и правильные заголовки")
    def test_extra_info_panel_include_phone_payment_comment_and_extra_wishes_fields(self,
                                                                                    driver_open_choose_taxi_panel):
        page = GetTaxiPage(driver_open_choose_taxi_panel)
        assert (
                page.get_text_from_extra_info_phone_field() == EXTRA_INFO_PHONE_FIELD_TEXT
                and page.get_text_from_extra_info_payment_field() == EXTRA_INFO_PAYMENT_INFO_TEXT
                and page.get_text_from_extra_info_comment_field() == EXTRA_INFO_COMMENT_FIELD_TEXT
                and page.get_text_from_extra_info_extra_wishes_field() == EXTRA_INFO_EXTRA_WISHES_TEXT
                and page.get_text_from_extra_info_get_taxi_button() == EXTRA_INFO_GET_TAXI_BUTTON_TEXT
        )
