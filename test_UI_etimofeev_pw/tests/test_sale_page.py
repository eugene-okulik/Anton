from test_UI_etimofeev_pw.pages.sale_page import SalePage


def test_button(page):
    collections_page = SalePage(page)
    collections_page.open()
    collections_page.check_current_url()
    collections_page.check_the_page_name()
    collections_page.check_open_sale_product()
