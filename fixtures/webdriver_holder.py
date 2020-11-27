import pytest
from webdrivermanager import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope="session")
def webdriver():
    chrome_driver = ChromeDriverManager()
    chrome_driver.download_and_install()
    driver = webdriver.Chrome(executable_path=chrome_driver.get_download_path())
    driver.get("https://www.fanduel.com/")
    driver.maximize_window()
    return driver
