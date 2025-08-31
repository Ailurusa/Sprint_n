from selenium.webdriver.common.by import By


class FinishRideLocators:
    HEADER_TITLE = (By.CSS_SELECTOR, ".order-header-title")
    VEHICLE_IMAGE = (By.XPATH, "//img[@alt='Car']")
    VEHICLE_PLATE = (By.CSS_SELECTOR, ".number")
    DRIVER_RATING_BTN = (By.CSS_SELECTOR, ".order-btn-rating")
    DRIVER_AVATAR = (By.XPATH, "//*[@class='order-btn-rating']/parent::*//img")
    DRIVER_NAME = (By.XPATH, "//*[@class='order-btn-rating']/ancestor::div[2]/div[2]")
    CANCEL_BUTTON = (By.XPATH, ".//div[text()='Отменить']/../button")
    CANCEL_BUTTON_LABEL = (By.XPATH, ".//div[text()='Отменить']")
    DETAILS_BUTTON = (By.XPATH, ".//div[text()='Детали']/../button")
    DETAILS_BUTTON_LABEL = (By.XPATH, ".//div[text()='Детали']")
    FARE_LABEL = (By.XPATH, "//*[contains(normalize-space(),'Стоимость -')]")
