from selenium.webdriver.common.by import By
from driver.DriverHolder import DriverHolder


def send_text(css_selector, content):
    element = DriverHolder.get_driver().find_element(By.CSS_SELECTOR, css_selector)
    element.send_keys(content)
