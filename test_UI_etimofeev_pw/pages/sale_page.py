from playwright.sync_api import expect

from test_UI_etimofeev_pw.pages.base_page import BasePage
from test_UI_etimofeev_pw.pages.locators.locators import SaleLocators as Loc


class SalePage(BasePage):
    page_url = "/sale.html"

    def check_current_url(self):
        expect(self.page).to_have_url(self.base_url + self.page_url)

    def check_the_page_name(self):
        expected_name = "Sale"
        current_name = self.find(Loc.NAME_OF_THE_PAGE)
        expect(current_name, "Names are different").to_contain_text(expected_name)

    def check_open_sale_product(self):
        women_deal_button = self.find(Loc.WOMEN_DEAL_BUTTON)
        women_deal_button.click()
        expect(self.page).to_have_url(
            "https://magento.softwaretestingboard.com/promotions/women-sale.html"
        )
