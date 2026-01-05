from stellarburgerPW.locators.draganddrop_locators import DragLocators as DL
@pytest.mark.smoke
def test_drag_and_drop(register_page):
    register_page.open()
    register_page.drag_and_drop(DL.C_BURGER, DL.D_BURGER)
    register_page.click_on_el(DL.SAUCES_TAB)
    register_page.drag_and_drop(DL.SAUCES_C, DL.D_BURGER)
    register_page.click_on_el(DL.NACHINKI_TAB)
    register_page.drag_and_drop(DL.NACHINKI_C, DL.D_BURGER)
