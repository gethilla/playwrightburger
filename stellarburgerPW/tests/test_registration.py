import pytest
from stellarburgerPW.tests.conftest import register_page
import time

@pytest.mark.smoke
def test_register_ui(register_page):
    register_page.open()
    register_page.click_on_el('text=Личный Кабинет')
    register_page.click_on_el('text=Зарегистрироваться')
    register_page.fill_register_fields()
    register_page.click_on_el('text=Зарегистрироваться')
    time.sleep(5)





