from stellarburgerPW.tests.conftest import login_page


def test_login_ui(login_page, auth_api):
    login_page.open()
    login_page.click_on_el('text=Личный кабинет')
    login_page.fill_login_fields(auth_api)
    login_page.click_on_el('text=Войти')