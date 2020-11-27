from helpers import click_actions, text_field_actions
from locators import login_page_locators


def fill_email_field(driver, text):
    text_field_actions.send_text(driver, login_page_locators.email_input_field, text)


def fill_password_field(driver, text):
    text_field_actions.send_text(driver, login_page_locators.password_input_field, text)


def submit_data(driver):
    click_actions.click_element(driver, login_page_locators.submit_button)
