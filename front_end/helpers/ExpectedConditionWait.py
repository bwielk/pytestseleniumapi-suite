from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from front_end.driver.DriverHolder import DriverHolder
from selenium.webdriver.common.by import By


class ExpectedConditionWait:

    @staticmethod
    def wait_until_element_clickable(locator):
        return WebDriverWait(DriverHolder.get_driver(), 30).\
            until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    @staticmethod
    def wait_until_element_visible(locator):
        return WebDriverWait(DriverHolder.get_driver(), 30).\
            until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    @staticmethod
    def wait_until_alert_visible():
        return WebDriverWait(DriverHolder.get_driver(), 30).\
            until(EC.alert_is_present())

    @staticmethod
    def wait_until_text_is_displayed(locator, text):
        return WebDriverWait(DriverHolder.get_driver(), 30).\
            until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, locator), text))
