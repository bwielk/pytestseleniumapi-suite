import pytest
from webdrivermanager import ChromeDriverManager
from selenium import webdriver


@pytest.fixture()
def gen_web_driver():
    chrome_driver = ChromeDriverManager()
    path_to_driver = chrome_driver.download_and_install()[0]
    driver = webdriver.Chrome(executable_path=path_to_driver)
    driver.get("https://www.fanduel.com/")
    driver.maximize_window()
    return driver
