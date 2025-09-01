import allure
from data import EXPECTED_TARIFFS_TAXI_LIST

from locators.taxi_tariff_locators import TaxiTariffLocators as L
from pages.base_page import BasePage


class GetTaxiPage(BasePage):

    def _find_all(self, locator):
        by, value = locator
        return self.browser.find_elements(by, value)

    @allure.step("Получаем имя активного тарифа")
    def get_active_tariff_name(self) -> str:
        self.wait_for_visibility(L.ACTIVE_TITLE)
        return self.extract_text(L.ACTIVE_TITLE).strip()

    @allure.step("Получаем список всех отображающихся тарифов")
    def get_tariff_names_list(self) -> list[str]:
        self.wait_for_visibility(L.CARD_TITLES)
        return [el.text.strip() for el in self._find_all(L.CARD_TITLES) if el.text.strip()]

    @allure.step("Проверяем, все ли ожидаемые тарифы отображаются в списке тарифов")
    def is_all_expected_tariffs_in_tariffs_names_list(self) -> bool:
        actual = set(self.get_tariff_names_list())
        expected = set(EXPECTED_TARIFFS_TAXI_LIST)
        return expected.issubset(actual)

    @allure.step("Проверяем, все ли отображающиеся тарифы есть в ТЗ")
    def is_all_visible_tariffs_is_expected(self) -> bool:
        actual = set(self.get_tariff_names_list())
        expected = set(EXPECTED_TARIFFS_TAXI_LIST)
        return actual.issubset(expected)

    @allure.step("Проверяем, что в списке тарифов есть активный тариф")
    def is_active_tariff_in_tariff_names_list(self) -> bool:
        active = self.get_active_tariff_name()
        all_tariffs = self.get_tariff_names_list()
        return active in all_tariffs

    @allure.step("Нажимаем на тариф Рабочий")
    def click_on_work_tariff(self):
        self.tap(L.TARIFF_WORK)

    @allure.step("Нажимаем на тариф Сонный")
    def click_on_sleep_tariff(self):
        self.tap(L.TARIFF_SLEEP)

    @allure.step("Нажимаем на тариф Отпускной")
    def click_on_holiday_tariff(self):
        self.tap(L.TARIFF_HOLIDAY)

    @allure.step("Нажимаем на тариф Разговорчивый")
    def click_on_talk_tariff(self):
        self.tap(L.TARIFF_TALKATIVE)

    @allure.step("Нажимаем на тариф Утешительный")
    def click_on_glad_tariff(self):
        self.tap(L.TARIFF_COMFORT)

    @allure.step("Нажимаем на тариф Глянцевый")
    def click_on_glam_tariff(self):
        self.tap(L.TARIFF_GLAM)

    @allure.step("Наводим курсор на иконку i для активной вкладки")
    def focus_on_info_icon(self):
        self.focus_on_element(L.ACTIVE_INFO_BUTTON)

    @allure.step("Проверяем, что отображается окно с подсказкой")
    def is_info_panel_visible(self) -> bool:
        return self.is_visible(L.ACTIVE_INFO_DESCRIPTION)

    @allure.step("Получаем заголовок окна с подсказкой")
    def get_info_panel_title(self) -> str:
        self.wait_for_visibility(L.ACTIVE_INFO_HEADER)
        return self.extract_text(L.ACTIVE_INFO_HEADER).strip()

    @allure.step("Получаем описание окна с подсказкой")
    def get_info_panel_description(self) -> str:
        self.wait_for_visibility(L.ACTIVE_INFO_DESCRIPTION)
        return self.extract_text(L.ACTIVE_INFO_DESCRIPTION).strip()

    @allure.step("Получаем текст поля Телефон")
    def get_text_from_extra_info_phone_field(self) -> str:
        self.wait_for_visibility(L.PHONE_HELP_TEXT)
        return self.extract_text(L.PHONE_HELP_TEXT).strip()

    @allure.step("Получаем текст поля Способ оплаты")
    def get_text_from_extra_info_payment_field(self) -> str:
        self.wait_for_visibility(L.PAYMENT_HELP_TEXT)
        return self.extract_text(L.PAYMENT_HELP_TEXT).strip()

    @allure.step("Получаем текст поля Комментарий водителю")
    def get_text_from_extra_info_comment_field(self) -> str:
        self.wait_for_visibility(L.COMMENT_LABEL)
        return self.extract_text(L.COMMENT_LABEL).strip()

    @allure.step("Получаем заголовок блока Требования к заказу")
    def get_text_from_extra_info_extra_wishes_field(self) -> str:
        self.wait_for_visibility(L.EXTRA_WISHES_HEADER)
        return self.extract_text(L.EXTRA_WISHES_HEADER).strip()

    @allure.step("Получаем текст кнопки Заказать такси")
    def get_text_from_extra_info_get_taxi_button(self) -> str:
        self.wait_for_visibility(L.REQUEST_TAXI_BUTTON)
        return self.extract_text(L.REQUEST_TAXI_BUTTON).strip()

    @allure.step("Раскрываем блок с требованиями к заказу")
    def click_on_extra_wishes_title(self):
        self.tap(L.EXTRA_WISHES_TOGGLE)

    @allure.step("Прокручиваем вниз панель с доп. опциями")
    def scroll_down_extra_panel(self):
        panel = self.get_element(L.EXTRA_INFO_PANEL)
        self.move_to_down_in_container(panel)

    @allure.step("Нажимаем на чекбокс «Столик для ноутбука»")
    def click_on_extra_wishes_laptop_checkbox(self):
        self.wait_for_visibility(L.LAPTOP_SWITCH)
        self.tap(L.LAPTOP_SWITCH)

    @allure.step("Нажимаем на кнопку «Заказать такси»")
    def click_on_extra_info_get_taxi_button(self):
        self.tap(L.REQUEST_TAXI_BUTTON)

    @allure.step("Получаем стоимость маршрута")
    def get_taxi_order_price(self) -> str:
        self.wait_for_visibility(L.ACTIVE_PRICE)
        text = self.extract_text(L.ACTIVE_PRICE).strip()
        return (text.split() or [""])[0]
