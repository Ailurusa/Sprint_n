import allure
from selenium.webdriver.common.keys import Keys

from locators.home_page_locators import HomePageLocators as L
from pages.base_page import BasePage


class MainPage(BasePage):
    def _find_all(self, locator):
        by, value = locator
        return self.browser.find_elements(by, value)

    def _is_not_disabled(self, locator) -> bool:
        el = self.get_element(locator)
        return not (el.get_attribute("disabled") or "disabled" in (el.get_attribute("class") or ""))

    @allure.step("Ввести адрес отправления")
    def enter_from_address(self, address: str):
        self.wait_for_visibility(L.FROM_INPUT)
        self.fill_field(L.FROM_INPUT, address)
        self.get_element(L.FROM_INPUT).send_keys(Keys.ENTER)

    @allure.step("Ввести адрес назначения")
    def enter_to_address(self, address: str):
        self.wait_for_visibility(L.TO_INPUT)
        self.fill_field(L.TO_INPUT, address)
        self.get_element(L.TO_INPUT).send_keys(Keys.ENTER)
        self.wait_for_visibility(L.ROUTE_PICKER)

    @allure.step("Получить список точек маршрута на карте")
    def get_route_pins(self):
        return self._find_all(L.MAP_ROUTE_PINS)

    @allure.step("Панель выбора маршрута отображается")
    def is_route_picker_visible(self) -> bool:
        return self.is_visible(L.ROUTE_PICKER)

    @allure.step("Список вкладок (режимов) маршрута")
    def list_mode_tabs(self):
        self.wait_for_visibility(L.ROUTE_PICKER)
        return self._find_all(L.MODE_TABS)

    @allure.step("Клик по вкладке «Оптимальный»")
    def click_tab_optimal(self):
        tabs = self.list_mode_tabs()
        tabs[0].click()

    @allure.step("Клик по вкладке «Быстрый»")
    def click_tab_fast(self):
        tabs = self.list_mode_tabs()
        tabs[1].click()

    @allure.step("Клик по вкладке «Свой»")
    def click_tab_custom(self):
        tabs = self.list_mode_tabs()
        tabs[2].click()

    @allure.step("Текст активной вкладки")
    def active_tab_text(self) -> str:
        self.wait_for_visibility(L.ACTIVE_MODE_TAB)
        return self.extract_text(L.ACTIVE_MODE_TAB).strip()

    @allure.step("Текст описания маршрута (стоимость)")
    def route_description_text(self) -> str:
        self.wait_for_visibility(L.RESULT_TEXT)
        return self.extract_text(L.RESULT_TEXT).strip()

    @allure.step("Текст длительности маршрута")
    def route_duration_text(self) -> str:
        self.wait_for_visibility(L.RESULT_DURATION)
        return self.extract_text(L.RESULT_DURATION).strip()

    @allure.step("Текст кнопки на панели результатов")
    def result_button_text(self) -> str:
        self.wait_for_visibility(L.RESULT_ACTION_BUTTON)
        return self.extract_text(L.RESULT_ACTION_BUTTON).strip()

    @allure.step("Нажать кнопку на панели результатов")
    def click_result_button(self):
        self.tap(L.RESULT_ACTION_BUTTON)

    @allure.step("Опция «Авто» доступна")
    def is_option_car_available(self) -> bool:
        return self._is_not_disabled(L.SELF_CAR)

    @allure.step("Опция «Пешком» доступна")
    def is_option_walk_available(self) -> bool:
        return self._is_not_disabled(L.SELF_WALK)

    @allure.step("Опция «Такси» доступна")
    def is_option_taxi_available(self) -> bool:
        return self._is_not_disabled(L.SELF_TAXI)

    @allure.step("Опция «Велосипед» доступна")
    def is_option_bike_available(self) -> bool:
        return self._is_not_disabled(L.SELF_BIKE)

    @allure.step("Опция «Самокат» доступна")
    def is_option_scooter_available(self) -> bool:
        return self._is_not_disabled(L.SELF_SCOOTER)

    @allure.step("Опция «Драйв» доступна")
    def is_option_drive_available(self) -> bool:
        return self._is_not_disabled(L.SELF_DRIVE)

    @allure.step("Все опции доступны")
    def are_all_options_available(self) -> bool:
        return all([
            self.is_option_car_available(),
            self.is_option_walk_available(),
            self.is_option_taxi_available(),
            self.is_option_bike_available(),
            self.is_option_scooter_available(),
            self.is_option_drive_available(),
        ])

    @allure.step("Выбрать опцию «Велосипед»")
    def select_option_bike(self):
        self.wait_for_visibility(L.SELF_BIKE)
        self.tap(L.SELF_BIKE)

    @allure.step("Выбрать опцию «Драйв»")
    def select_option_drive(self):
        self.wait_for_visibility(L.SELF_DRIVE)
        self.tap(L.SELF_DRIVE)
