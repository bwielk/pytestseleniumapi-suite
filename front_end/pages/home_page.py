from front_end.helpers import click_actions, browser_helper
from front_end.locators import home_page_locators


def open_main_page():
    browser_helper.open_url("https://www.autohero.com/de/")


def click_login_page():
    click_actions.click_element(home_page_locators.log_in_button)


def select_login_option():
    click_actions.click_element(home_page_locators.account_option)
