import pytest
from selenium.webdriver.common.by import By
from webdrivermanager import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope="session")
def gen_web_driver():
    chrome_driver = ChromeDriverManager()
    chrome_driver.download_and_install()
    driver = webdriver.Chrome(executable_path=chrome_driver.get_download_path())
    driver.get("https://www.fanduel.com/")
    driver.maximize_window()
    element = driver.find_element(By.CSS_SELECTOR, "css_selector")
    element.send_keys()
    return driver
