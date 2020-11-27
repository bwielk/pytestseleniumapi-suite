from selenium.webdriver.common.by import By


def send_text(driver, css_selector, content):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    element.send_keys(content)
