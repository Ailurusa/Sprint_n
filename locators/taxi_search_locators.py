from selenium.webdriver.common.by import By


class TaxiSearchLocators:
    HEADER_TITLE = (By.CSS_SELECTOR, ".order-header-title")
    HEADER_TIMER = (By.CSS_SELECTOR, ".order-header-time")
    CANCEL_BUTTON = (By.XPATH, "//button[./div[normalize-space()='Отменить']]")
    CANCEL_BUTTON_LABEL = (By.XPATH, ".//div[text()='Отменить']")
    DETAILS_BUTTON = (By.XPATH, "//button[./div[normalize-space()='Детали']]")
    DETAILS_BUTTON_LABEL = (By.XPATH, ".//div[text()='Детали']")
