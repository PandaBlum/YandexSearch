import time
from pages.base_page import BasePage
from pages.locators import *

list_images = []


class PicturesPage(BasePage):
    def should_be_pictures_url(self):
        '''
        ПРОВЕРКА:
        Проверка на корректность ссылки
        '''
        assert "images/" in self.url, "Link does not match"

    def getting_a_category_of_pictures(self, serial_number):
        '''
        ШАБЛОН:
        Получение категории картинок
        '''
        serial_number -= 1
        search = self.browser.find_elements(*PicturesPageLocators.GET_CATEGORY)
        self.search_query = search[serial_number].text
        return search[serial_number]

    def action_a_category_of_pictures(self, serial_number):
        """
        ДЕЙСТВИЕ:
        Переход по категории в Яндекс.Картинки
        """
        category = self.getting_a_category_of_pictures(serial_number)
        category.click()
        time.sleep(5)

    def should_be_category_open(self):
        '''
        ПРОВЕРКА:
        Проверка на то, что категория картинок открыта
        '''
        search = self.browser.find_element(*PicturesPageLocators.TITLE)
        search = search.get_attribute('text').split(":")
        assert search[0] == self.search_query, "search query does not match the category"

    def action_a_picture(self, serial_number):
        """
        ДЕЙСТВИЕ:
        Открытие изображения
        """
        serial_number -= 1
        search = self.browser.find_elements(
            *PicturesPageLocators.CONTENT_IMAGE)
        url_pictures = search[0].get_attribute("href")
        self.browser.get(url_pictures)
        url_pictures = self.browser.find_element(
            *PicturesPageLocators.OPEN_IMAGE)
        list_images.append(url_pictures.get_attribute("href"))
        time.sleep(2)

    def action_a_next_picture(self):
        """
        ДЕЙСТВИЕ:
        Открытие следующего изображения
        """
        button = self.browser.find_element(
            *PicturesPageLocators.NEXT_BUTTON)
        button.click()
        url_pictures = self.browser.find_element(
            *PicturesPageLocators.OPEN_IMAGE)
        list_images.append(url_pictures.get_attribute("href"))
        time.sleep(2)

    def should_be_next_picture(self):
        '''
        ПРОВЕРКА:
        Проверка на смену изображения
        '''
        assert list_images[0] != list_images[1], "image links are the same"

    def action_a_prev_picture(self):
        """
        ДЕЙСТВИЕ:
        Открытие предыдущего изображения
        """
        button = self.browser.find_element(
            *PicturesPageLocators.PREV_BUTTON)
        button.click()

    def should_be_prev_picture(self):
        '''
        ПРОВЕРКА:
        Проверка на то, что первое изображение было предыдущим
        '''
        url_pictures = self.browser.find_element(
            *PicturesPageLocators.OPEN_IMAGE)
        assert url_pictures.get_attribute(
            "href") == list_images[0], "This is not the same picture!!!!"
