from selenium.webdriver.common.by import By
from front_end.driver.DriverHolder import DriverHolder


def check_content(css_selector, expected_content):
    element = DriverHolder.get_driver().find_element(By.CSS_SELECTOR, css_selector)
    assert element.text == expected_content
