import requests
from . import BASE_URL


class UserApi:
    def __init__(self, api_key):
        self.headers = {
            "Authorization": f"Token token={api_key}",
            "Content-Type": "application/json",
        }
        self.user_token = None

    def create_user(self, login, email, password):
        url = f"{BASE_URL}/users"

        headers = self.headers
        headers.update({
            "Content-Type": "application/json",
        })

        body = {
            "user": {
                "login": login,
                "email": email,
                "password": password
            }
        }

        return requests.post(url, json=body, headers=headers)

    def get_user(self, login):
        url = f"{BASE_URL}/users/{login}"

        headers = self.headers
        headers.update({
            "User-Token": self.user_token
        })

        return requests.get(url, headers=headers)

    def update_user(self, curr_login, **kwargs):
        body = {
            "user": {}
        }

        for key, value in kwargs.items():
            body["user"].update({key: value})

        url = f"{BASE_URL}/users/{curr_login}"

        headers = self.headers
        headers.update({
            "User-Token": self.user_token
        })

        return requests.put(url, json=body, headers=headers)
