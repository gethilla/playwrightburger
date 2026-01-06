import allure
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, base_url):
        self.page = page
        self.base_url = base_url



    @allure.suite('open page')
    def open(self):
        self.page.goto(self.base_url)

    @allure.step('click on element')
    def click_on_el(self, locator):
        self.page.click(selector=locator)

    @allure.step('fill fields')
    def fill_field(self, locator, text):
        self.page.fill(selector=locator, value=text)



