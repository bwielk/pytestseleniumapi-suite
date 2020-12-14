from front_end.helpers import click_actions, text_field_actions, element_checks
from front_end.locators import login_page_locators
from front_end.content import login_page_content


def fill_email_field(text):
    text_field_actions.send_text(login_page_locators.email_input_field, text)


def fill_password_field(text):
    text_field_actions.send_text(login_page_locators.password_input_field, text)


def submit_data():
    click_actions.click_element(login_page_locators.submit_button)


def check_failed_login_content():
    element_checks.check_content(login_page_locators.login_error, login_page_content.failed_login)


def confirm_account():
    element_checks.check_content(login_page_locators.confirm_email_section, login_page_locators.confirm_email_section)
