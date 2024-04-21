from ..api.user_api import UserApi
from ..helper import gen_rand_email, gen_rand_str

def test_user_created(rand_user, api_key):
    user_api = UserApi(api_key)
    response = user_api.create_user(rand_user["login"], rand_user["email"], rand_user["password"])

    create_body: dict = response.json()

    assert response.status_code == 200
    assert "error_code" not in tuple(create_body.keys())
    assert create_body["login"] == rand_user["login"]

    user_api.user_token = create_body["User-Token"]
    response = user_api.get_user(rand_user["login"])

    get_body: dict = response.json()

    assert response.status_code == 200
    assert "error_code" not in tuple(get_body.keys())
    assert create_body["login"] == get_body["login"]
    assert get_body["account_details"]["email"] == rand_user["email"]

def test_user_updated(rand_user, api_key):
    user_api = UserApi(api_key)
    response = user_api.create_user(rand_user["login"], rand_user["email"], rand_user["password"])

    create_body: dict = response.json()

    assert response.status_code == 200
    assert "error_code" not in tuple(create_body.keys())
    assert create_body["login"] == rand_user["login"]

    updated_login = gen_rand_str(2, 19)
    updated_email = gen_rand_email()

    user_api.user_token = create_body["User-Token"]
    response = user_api.update_user(create_body["login"], login=updated_login, email=updated_email)

    updated_body: dict =  response.json()

    assert response.status_code == 200
    assert "error_code" not in tuple(updated_body.keys())
    assert updated_body["message"] == "User successfully updated."

    response = user_api.get_user(updated_login)

    get_body: dict = response.json()

    assert response.status_code == 200
    assert "error_code" not in tuple(get_body.keys())
    assert get_body["login"] == updated_login
    assert get_body["account_details"]["email"] == updated_email
