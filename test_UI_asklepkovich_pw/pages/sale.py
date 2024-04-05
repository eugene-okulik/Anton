from test_UI_asklepkovich_pw.pages.base_page import BasePage
from test_UI_asklepkovich_pw.pages.locators import sele_locators as loc


class Sale(BasePage):
    page_url = '/sale.html'
    page_women_url = '/women-sale.html'
    page_men_bargains = 'promotions/men-sale.html'
    page_gear = 'gear.html'

    def check_click_button_url_women(self):
        button_women_shop = self.find(loc.shop_women_deals)
        button_women_shop.click()
        self.wait_full_to_load()
        assert self.page_women_url in self.page.url, f'Error page {self.page_women_url} not found'


    def check_men_bargains(self):
        bargains = self.find(loc.men_bargains)
        bargains.click()
        self.wait_full_to_load()
        assert self.page_men_bargains in self.page.url, f'Error page {self.page_men_bargains} not found'


    def luma_gear_steals(self):
        luma = self.find(loc.luma_gear_steals)
        self.title = luma.locator(loc.title).text_content()
        self.info = luma.locator(loc.info).text_content()
        self.more_icon = luma.locator(loc.more_icon).text_content()
        print(f'text={self.info}')
        luma.click()
        assert self.page_gear in self.page.url, f'Error page {self.page_gear} not found\n'
