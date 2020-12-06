from models import home_page, login_page


class TestSearch:

    def test_failed_login_message_is_correct(self):
        home_page.open_main_page()
        home_page.click_login_page()
        home_page.select_fantasy_login_option()
        login_page.fill_email_field("hello@hello.com")
        login_page.fill_password_field("password")
        login_page.check_failed_login_content()
