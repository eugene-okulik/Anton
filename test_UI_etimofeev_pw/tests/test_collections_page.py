from test_UI_etimofeev_pw.pages.collections_page import CollectionsPage


def test_button(page):
    collections_page = CollectionsPage(page)
    collections_page.open()
    collections_page.check_current_url()
    collections_page.check_the_page_name()
    collections_page.check_switching_pages()
