import os
import pytest
from dotenv import load_dotenv
from .helper import gen_rand_str, gen_rand_email


@pytest.fixture(scope="session")
def api_key() -> str:
    load_dotenv()
    return os.getenv("API_KEY")

@pytest.fixture
def rand_user() -> dict[str]:
    login = gen_rand_str(2, 19)
    email = gen_rand_email()
    password = gen_rand_str(5, 120)
    return {
        "login": login,
        "email": email,
        "password": password
    }
