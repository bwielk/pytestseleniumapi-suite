from selenium.webdriver.common.by import By
from driver.DriverHolder import DriverHolder


def click_element(css_selector):
    DriverHolder.get_driver().find_element(By.CSS_SELECTOR, css_selector)

