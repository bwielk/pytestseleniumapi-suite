from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverHolder:

    driver = None

    @staticmethod
    def generate_driver():
        if DriverHolder.driver is None:
            DriverHolder.driver = webdriver.Chrome(ChromeDriverManager().install())
            DriverHolder.driver.maximize_window()

    @staticmethod
    def get_driver():
        if DriverHolder.driver is not None:
            return DriverHolder.driver
        else:
            DriverHolder.generate_driver()