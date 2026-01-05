from playwright.sync_api import Page, expect
import allure

class Assertions:
    def __init__(self, page:Page):
        self.page = page

    @allure.step('')
    def check_current_url(self, url):
        expect(self.page).to_have_url(url)
