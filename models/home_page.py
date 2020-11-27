from helpers import click_actions
from locators import home_page_locators


def click_login_page(driver):
    click_actions.click_element(driver, home_page_locators.log_in_button)


def select_fantasy_login_option(driver):
    click_actions.click_element(driver, home_page_locators.fantasy_option)


def select_sportsbook_login_option(driver):
    click_actions.click_element(driver, home_page_locators.sportsbook_option)
