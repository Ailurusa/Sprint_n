from selenium.webdriver.common.by import By


class TaxiTariffLocators:
    CARD_TITLES = (By.CSS_SELECTOR, ".tcard-title")
    ACTIVE_TITLE = (By.CSS_SELECTOR, ".tcard.active .tcard-title")
    ACTIVE_INFO_BUTTON = (By.CSS_SELECTOR, ".tcard.active .i-button.tcard-i.active")
    ACTIVE_INFO_HEADER = (By.CSS_SELECTOR, ".tcard.active .i-title")
    ACTIVE_INFO_DESCRIPTION = (By.CSS_SELECTOR, ".tcard.active .i-dPrefix")
    ACTIVE_PRICE = (By.CSS_SELECTOR, ".tcard.active .tcard-price")
    TARIFF_WORK = (By.XPATH, "//div[@class='tariff-cards']//div[normalize-space()='Рабочий']")
    TARIFF_SLEEP = (By.XPATH, "//div[@class='tariff-cards']//div[normalize-space()='Сонный']")
    TARIFF_HOLIDAY = (By.XPATH, "//div[@class='tariff-cards']//div[normalize-space()='Отпускной']")
    TARIFF_TALKATIVE = (By.XPATH, "//div[@class='tariff-cards']//div[normalize-space()='Разговорчивый']")
    TARIFF_COMFORT = (By.XPATH, "//div[@class='tariff-cards']//div[normalize-space()='Утешительный']")
    TARIFF_GLAM = (By.XPATH, "//div[@class='tariff-cards']//div[normalize-space()='Глянцевый']")
    EXTRA_INFO_PANEL = (By.CSS_SELECTOR, ".tariff-picker.shown")
    PHONE_HELP_TEXT = (By.CSS_SELECTOR, ".np-text")
    PAYMENT_HELP_TEXT = (By.CSS_SELECTOR, ".pp-text")
    COMMENT_LABEL = (By.XPATH, "//input[@id='comment']/parent::*//label")
    EXTRA_WISHES_HEADER = (By.CSS_SELECTOR, ".reqs-head")
    EXTRA_WISHES_TOGGLE = (By.CSS_SELECTOR, ".reqs-arrow")
    REQUEST_TAXI_BUTTON = (By.CSS_SELECTOR, ".smart-button-main")
    LAPTOP_SWITCH = (By.CSS_SELECTOR, ".slider.round")
