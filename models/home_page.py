from helpers import click_actions, browser_helper
from locators import home_page_locators


def open_main_page():
    browser_helper.open_url("https://www.fanduel.com/")


def click_login_page():
    click_actions.click_element(home_page_locators.log_in_button)


def select_fantasy_login_option():
    click_actions.click_element(home_page_locators.fantasy_option)


def select_sportsbook_login_option():
    click_actions.click_element(home_page_locators.sportsbook_option)
