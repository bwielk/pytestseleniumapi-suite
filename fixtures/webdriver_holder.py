import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def gen_web_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.fanduel.com/")
    driver.maximize_window()
    return driver
