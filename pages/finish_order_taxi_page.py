import allure

from locators.finish_ride_locators import FinishRideLocators as L
from pages.base_page import BasePage


class FinishOrderTaxiPage(BasePage):
    @allure.step("Получаем текст заголовка панели завершения заказа")
    def get_title_text(self) -> str:
        self.wait_for_visibility(L.HEADER_TITLE)
        return self.extract_text(L.HEADER_TITLE).strip()

    @allure.step("Проверяем, что отображается картинка с машиной")
    def is_car_picture_visible(self) -> bool:
        return self.is_visible(L.VEHICLE_IMAGE)

    @allure.step("Проверяем, что картинка с машиной не отображается")
    def is_car_picture_invisible(self) -> bool:
        return self.is_invisible(L.VEHICLE_IMAGE)

    @allure.step("Проверяем, что отображается валидный номер машины")
    def is_car_number_valid(self) -> bool:
        self.wait_for_visibility(L.VEHICLE_PLATE)
        plate = self.extract_text(L.VEHICLE_PLATE).strip()
        return len(plate) == 8

    @allure.step("Проверяем, что отображается аватар водителя")
    def is_driver_picture_visible(self) -> bool:
        return self.is_visible(L.DRIVER_AVATAR)

    @allure.step("Проверяем, что отображается рейтинг водителя")
    def is_rating_visible(self) -> bool:
        return self.is_visible(L.DRIVER_RATING_BTN)

    @allure.step("Проверяем, что отображается имя водителя")
    def is_driver_name_visible_and_not_empty(self) -> bool:
        self.wait_for_visibility(L.DRIVER_NAME)
        name = self.extract_text(L.DRIVER_NAME).strip()
        return bool(name)

    @allure.step("Получаем текст кнопки «Отменить»")
    def get_return_button_text(self) -> str:
        self.wait_for_visibility(L.CANCEL_BUTTON_LABEL)
        return self.extract_text(L.CANCEL_BUTTON_LABEL)

    @allure.step("Получаем текст кнопки «Детали»")
    def get_details_button_text(self) -> str:
        self.wait_for_visibility(L.DETAILS_BUTTON_LABEL)
        return self.extract_text(L.DETAILS_BUTTON_LABEL)

    @allure.step("Кликаем на кнопку «Отменить»")
    def click_on_return_button(self):
        self.tap(L.CANCEL_BUTTON)

    @allure.step("Кликаем на кнопку «Детали»")
    def click_on_details_button(self):
        self.tap(L.DETAILS_BUTTON)

    @allure.step("Получаем текст «Стоимость - X рублей»")
    def get_text_details_order_price(self) -> str:
        self.wait_for_visibility(L.FARE_LABEL)
        return self.extract_text(L.FARE_LABEL).strip()
