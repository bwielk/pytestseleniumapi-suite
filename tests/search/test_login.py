from models import home_page, login_page

class TestSearch:

    def test_failed_login_message_is_correct(self, gen_web_driver):
        home_page.click_login_page(gen_web_driver)
        home_page.select_fantasy_login_option(gen_web_driver)
        login_page.fill_email_field("hello@hello.com")
        login_page.fill_password_field("password")
        login_page.check_failed_login_content(gen_web_driver)
