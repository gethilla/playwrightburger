class DragLocators:
    C_BURGER = "//a[@draggable='true' and .//img[@alt='Флюоресцентная булка R2-D3']]"
    D_BURGER = "//section[contains(@class, 'BurgerConstructor')]/ul"

    SAUCES_TAB = "//div[contains(@class, 'tab_tab__')][.//span[text()='Соусы']]"
    SAUCES_C = "//a[@draggable='true' and .//img[@alt='Соус Spicy-X']]"

    NACHINKI_TAB = "//div[contains(@class, 'tab')][.//span[text()='Начинки']]"
    NACHINKI_C = "//a[@draggable='true' and .//img[@alt='Мясо бессмертных моллюсков Protostomia']]"
    SUBMIT_ORDER = "//button[contains(@class, 'button_button__33qZ0')][.//span(text()='Оформить заказ']]"