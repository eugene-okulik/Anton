from playwright.sync_api import expect

from test_UI_etimofeev_pw.pages.base_page import BasePage
from test_UI_etimofeev_pw.pages.locators.locators import CollectionsLocators as Loc


class CollectionsPage(BasePage):
    page_url = "/collections/eco-friendly.html"

    def check_current_url(self):
        expect(self.page).to_have_url(self.base_url + self.page_url)

    def check_the_page_name(self):
        expected_name = "Eco Friendly"
        current_name = self.find(Loc.NAME_OF_THE_PAGE)
        expect(current_name, "Names aren't matched").to_contain_text(expected_name)

    def check_switching_pages(self):
        next_page_button = self.find(Loc.NEXT_PAGE_BUTTON).last
        next_page_button.click()
        expect(self.page).to_have_url(
            "https://magento.softwaretestingboard.com/collections/eco-friendly.html?p=2"
        )
