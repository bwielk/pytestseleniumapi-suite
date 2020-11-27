from selenium.webdriver.common.by import By


def check_content(driver, css_selector, expected_content):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    assert element.text == expected_content
