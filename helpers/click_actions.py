from selenium.webdriver.common.by import By


def click_element(driver, css_selector):
    driver.find_element(By.CSS_SELECTOR, css_selector)

