from front_end.pages import home_page, login_page
from api.clients import user_service
from uuid import uuid4


class TestSearch:

    def test_failed_login_message_is_correct(self):
        user = user_service.get_users()[0]
        user_email = user["email"]
        user_password = user["username"] + str(user["id"]) + str(uuid4().time)
        home_page.open_main_page()
        home_page.click_login_page()
        home_page.select_login_option()
        login_page.fill_email_field(user_email)
        login_page.submit_data()
        login_page.fill_password_field(user_password)
        login_page.submit_data()
        login_page.check_failed_login_content()
