from api.helpers.request_helpers import simple_get

USER_SERVICE_URL = "https://jsonplaceholder.typicode.com/"
GET_USERS_URL = USER_SERVICE_URL + "users"


def get_users():
    return simple_get(GET_USERS_URL)