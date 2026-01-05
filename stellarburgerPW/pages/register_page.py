from stellarburgerPW.pages.basepage import BasePage
from playwright.sync_api import Page
from stellarburgerPW.locators.register_locators import RegisterLocators as RL
import allure


class RegisterPage(BasePage):
    def __init__(self, page:Page, base_url):
        super().__init__(page, base_url)


    @allure.step('register fields')
    def fill_register_fields(self):
        self.fill_field(locator=RL.NAME_FIELD, text='SashaAQA')
        self.fill_field(locator=RL.EMAIL_FIELD, text='sashaaqa@mail.ru')
        self.fill_field(locator=RL.PASSWORD_FIELD, text='1234567')

    @allure.step('drag and drop')
    def drag_and_drop(self, source_locator: str, target_locator: str):
        self.page.locator(source_locator).drag_to(self.page.locator(target_locator))



