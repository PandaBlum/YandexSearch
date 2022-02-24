import time
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from pages.locators import *


class SearchPage(BasePage):
    def should_be_field_search(self):
        '''
        ПРОВЕРКА:
        Наличие поля поиска
        '''
        assert self.is_element_present(
            *MainPageLocators.SEARCH_FIELD), "The field search is not found"

    def entering_a_query_in_the_search_field(self, query):
        '''
        ДЕЙСТВИЕ:
        Ввод в текста в поиск
        '''
        field_search = self.browser.find_element(
            *MainPageLocators.SEARCH_FIELD)
        field_search.send_keys(query)

    def list_suggest(self):
        """
        ПРОВЕРКА:
        Проверка наличия таблицы с подсказками
        """
        assert self.is_element_present(
            *MainPageLocators.HINT_TABLE), "no hints table"

    def start_search(self):
        """
        ПРОВЕРКА:
        Отправка запроса на поиск
        """
        field = self.browser.find_element(
            *MainPageLocators.SEARCH_FIELD)
        field.send_keys(Keys.ENTER)

    def should_be_results_table(self):
        '''
        ПРОВЕРКА:
        Проверка наличия таблицы с результатами
        '''
        assert self.is_element_present(
            *MainPageLocators.TABLE_RESULT), "Result search is not found"
        time.sleep(5)

    def should_be_found_links(self):
        '''
        ПРОВЕРКА:
        Проверка первых пяти ссылок
        '''
        search_result = self.browser.find_elements(
            *MainPageLocators.TABLE_RESULT)
        for i in range(4):
            item = search_result[i].text
            if "tensor.ru" in item:
                print(f"В сссылке {i} есть tensor.ru")
            else:
                print("Ссылки нет")
            assert "tensor.ru" in item, "link is not the same as tensor.ru"

    def element_services(self, serial_number):
        """
        ШАБЛОН:
        Получение ссылки сервиса
        """
        serial_number -= 1
        field_search = self.browser.find_element(
            *MainPageLocators.LIST_SERVICES)
        services = field_search.text
        services = services.split("\n")
        get_link_pictures = self.browser.find_element(
            By.LINK_TEXT, services[serial_number])
        return get_link_pictures.get_attribute("href")

    def should_be_element_pictures(self, serial_number, link):
        """
        ПРОВЕРКА:
        Проверка наличия ссылки
        """
        assert link in self.element_services(
            serial_number), f"Link {link} not found"

    def action_element_services(self, serial_number):
        """
        ДЕЙСТВИЕ:
        Переход по указанному сервису
        """
        link = self.element_services(serial_number)
        self.browser.get(link)
