import pytest
from playwright.sync_api import sync_playwright
from stellarburgerPW.base.main_page import MainUrl as MU
from stellarburgerPW.pages.login_page import LoginPage
from stellarburgerPW.pages.register_page import RegisterPage
import requests


@pytest.fixture(scope="session")
def auth_api():
    payload = {
        "email": "santi@mail.ru",
        "password": "123456"
}
    response = requests.post(
        f'{MU.BASE_URL}{MU.API_LOGIN}',
        json=payload
    )
    assert response.status_code == 200, response.text
    access_token = response.json()["accessToken"]

    return {
        "email": payload["email"],
        "password": payload["password"],
        "access_token": response.json()["accessToken"]
    }


@pytest.fixture(scope="function")
def page_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=700)
        page = browser.new_page()
        page.goto(MU.BASE_URL)
        yield page
        browser.close()

@pytest.fixture
def register_page(page_browser):
    return RegisterPage(page_browser, base_url=MU.BASE_URL)

@pytest.fixture(scope="function")
def login_page(page_browser, auth_api):
    login_page = LoginPage(page_browser, base_url=MU.BASE_URL)
    login_page.auth_data = auth_api
    return login_page





