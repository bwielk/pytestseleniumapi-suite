from driver.DriverHolder import DriverHolder


def open_url(url_string):
    DriverHolder.get_driver().get(url_string)