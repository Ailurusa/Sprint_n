from selenium.webdriver.common.by import By


class HomePageLocators:
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    ROUTE_PICKER = (By.XPATH, "//div[contains(@class,'type-picker') and contains(@class,'shown')]")
    MODE_TABS = (By.XPATH, "//div[@class='modes-container']/div[contains(@class,'mode')]")
    ACTIVE_MODE_TAB = (By.XPATH, "//div[contains(@class,'mode') and contains(@class,'active')]")
    RESULT_ACTION_BUTTON = (By.XPATH, "//div[@class='results-container']//button")
    RESULT_TEXT = (By.CLASS_NAME, "text")
    RESULT_DURATION = (By.CLASS_NAME, "duration")
    SELF_CAR = (By.XPATH, "//img[contains(@src,'car.')]/parent::*")
    SELF_WALK = (By.XPATH, "//img[contains(@src,'walk')]/parent::*")
    SELF_TAXI = (By.XPATH, "//img[contains(@src,'taxi')]/parent::*")
    SELF_BIKE = (By.XPATH, "//img[contains(@src,'bike')]/parent::*")
    SELF_SCOOTER = (By.XPATH, "//img[contains(@src,'scooter')]/parent::*")
    SELF_DRIVE = (By.XPATH, "//img[contains(@src,'drive')]/parent::*")
    MAP_ROUTE_PINS = (By.XPATH, "//ymaps[contains(@class,'route-pin__text')]/ymaps[@id]")
