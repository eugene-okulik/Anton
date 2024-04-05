import re
from test_UI_asklepkovich_pw.pages.base_page import BasePage
from test_UI_asklepkovich_pw.pages.locators import eco_friendly_locators as loc_eco


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'
    find_item = None

    def select_sort(self, value):
        selected = self.find(loc_eco.sort).first
        selected.select_option(value)
        self.wait_full_to_load()
        items = self.find(loc_eco.product).all_text_contents()
        list_exp = items
        match value:
            case 'price':
                find_price = re.compile(r"\$[0-9]+\.[0-9]{2}")
                prices = [
                    match.group().replace('$', '') for item in list_exp
                    if (match := find_price.search(item))
                ]
                self.screenshot()
                self.assert_check(prices, sorted(prices), f'Error sorted {value}')
            case 'name':
                names = list(map(lambda item: item.split('\n'), list_exp))
                names_sort = list(map(lambda item: item[3], names))
                self.screenshot()
                self.assert_check(names_sort, sorted(names_sort), f'Error sorted {value}')

# currently unused
    def choose_color(self, color):
        self.wait_full_to_load()
        self.find_item = self.find(loc_eco.product_details).first
        color_chose = self.find_item.locator(f'[option-label="{color}"]')
        color_chose.click()

    def add_to_cart(self):
        self.page.hover(loc_eco.product_selector)
        self.page.click(loc_eco.add_to_cart)
