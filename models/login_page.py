from helpers import click_actions, text_field_actions, element_checks
from locators import login_page_locators
from content import login_page_content


def fill_email_field(driver, text):
    text_field_actions.send_text(driver, login_page_locators.email_input_field, text)


def fill_password_field(driver, text):
    text_field_actions.send_text(driver, login_page_locators.password_input_field, text)


def submit_data(driver):
    click_actions.click_element(driver, login_page_locators.submit_button)


def check_failed_login_content(driver):
    element_checks.check_content(driver, login_page_locators.login_error, login_page_content.failed_login)
