import pytest
from front_end.driver.DriverHolder import DriverHolder


@pytest.fixture(autouse=True)
def gen_web_driver():
    DriverHolder.generate_driver()
    yield
    DriverHolder.get_driver().close()
