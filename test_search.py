from pages.search_page import SearchPage
from pages.pictures_page import PicturesPage

general_page = "https://yandex.ru"
pictures_page = "https://yandex.ru/images/"


def test_search_to_yandex(browser):
    page = SearchPage(browser, general_page)
    page.open()
    page.should_be_field_search()
    page.entering_a_query_in_the_search_field('Тензор')
    page.list_suggest()
    page.start_search()
    page.should_be_results_table()


def test_pictures_to_yandex(browser):
    page = SearchPage(browser, general_page)
    page.open()
    page.should_be_element_pictures(3, pictures_page)
    page.action_element_services(3)
    page = PicturesPage(browser, pictures_page)
    page.should_be_pictures_url()
    page.action_a_category_of_pictures(1)
    page.should_be_category_open()
    page.action_a_picture(1)
    page.action_a_next_picture()
    page.should_be_next_picture()
    page.action_a_prev_picture()
    page.should_be_prev_picture()
