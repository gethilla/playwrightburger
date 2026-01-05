from stellarburgerPW.tests.conftest import login_page
from stellarburgerPW.locators.draganddrop_locators import DragLocators as DL

def test_login_ui(login_page, auth_api, register_page):
    login_page.open()
    login_page.click_on_el('text=Личный кабинет')
    login_page.fill_login_fields(auth_api)
    login_page.click_on_el('text=Войти')
    register_page.open()
    register_page.drag_and_drop(DL.C_BURGER, DL.D_BURGER)
    register_page.click_on_el(DL.SAUCES_TAB)
    register_page.drag_and_drop(DL.SAUCES_C, DL.D_BURGER)
    register_page.click_on_el(DL.NACHINKI_TAB)
    register_page.drag_and_drop(DL.NACHINKI_C, DL.D_BURGER)
    register_page.click_on_el('text=Оформить заказ')