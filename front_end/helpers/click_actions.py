from selenium.webdriver.common.by import By
from front_end.driver.DriverHolder import DriverHolder


def click_element(css_selector):
    DriverHolder.get_driver().find_element(By.CSS_SELECTOR, css_selector)

