import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from data import BASE_URL, FIRST_ADDRESS, SECOND_ADDRESS
from pages.finish_order_taxi_page import FinishOrderTaxiPage
from pages.get_taxi_page import GetTaxiPage
from pages.main_page import MainPage
from pages.search_taxi_page import SearchTaxiPage


@pytest.fixture
def driver():
    with allure.step("Открыть браузер и перейти на главную страницу"):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        drv = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        drv.maximize_window()
        drv.get(BASE_URL)
        yield drv
        drv.quit()


@pytest.fixture
def driver_with_addresses(driver):
    with allure.step("Ввести адреса отправления и назначения"):
        page = MainPage(driver)
        page.enter_from_address(FIRST_ADDRESS)
        page.enter_to_address(SECOND_ADDRESS)
    yield driver


@pytest.fixture
def driver_option_bike(driver_with_addresses):
    page = MainPage(driver_with_addresses)
    with allure.step("Выбрать тариф «Свой» → опция «Велосипед»"):
        page.click_tab_custom()
        page.select_option_bike()
    yield driver_with_addresses


@pytest.fixture
def driver_open_choose_taxi_panel(driver_with_addresses):
    page = MainPage(driver_with_addresses)
    with allure.step("Открыть панель выбора такси: вкладка «Быстрый» → кнопка действия"):
        page.click_tab_fast()
        page.click_result_button()
    yield driver_with_addresses


@pytest.fixture
def driver_open_search_taxi_panel(driver_open_choose_taxi_panel):
    page = GetTaxiPage(driver_open_choose_taxi_panel)
    with allure.step(
            "Настроить заказ: тариф «Рабочий», раскрыть требования, включить «Столик для ноутбука», нажать «Заказать такси»"):
        page.click_on_work_tariff()
        page.click_on_extra_wishes_title()
        page.scroll_down_extra_panel()
        page.click_on_extra_wishes_laptop_checkbox()
        page.click_on_extra_info_get_taxi_button()
    yield driver_open_choose_taxi_panel


@pytest.fixture
def driver_open_finish_order_taxi_panel(driver_open_choose_taxi_panel):
    get_taxi_panel = GetTaxiPage(driver_open_choose_taxi_panel)
    with allure.step("Выбрать тариф «Рабочий» и запомнить цену"):
        get_taxi_panel.click_on_work_tariff()
        price = get_taxi_panel.get_taxi_order_price()
    with allure.step("Нажать «Заказать такси» и дождаться окончания поиска"):
        get_taxi_panel.click_on_extra_info_get_taxi_button()
        search_panel = SearchTaxiPage(driver_open_choose_taxi_panel)
        search_panel.wait_timer_finish()
    with allure.step("Убедиться, что панель завершения заказа открылась"):
        finish_panel = FinishOrderTaxiPage(driver_open_choose_taxi_panel)
        finish_panel.wait_opened()
    yield driver_open_choose_taxi_panel, price
