from selenium.webdriver.common.by import By


class MainPageLocators():
    # Главная страница Yandex
    SEARCH_FIELD = (By.ID, "text")
    HINT_TABLE = (By.CLASS_NAME, "body_search_yes")
    TABLE_RESULT = (By.CLASS_NAME, "serp-item")
    LINK_CARD = (By.CLASS_NAME, "link")
    LIST_SERVICES = (By.CLASS_NAME, "services-new__list")


class PicturesPageLocators():
    # Яндекс.Картинки
    GET_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item")
    TITLE = (By.XPATH, "/html/head/title")
    CONTENT_IMAGE = (By.CLASS_NAME, "serp-item__link")
    OPEN_IMAGE = (By.CLASS_NAME, "MMButton")
    NEXT_BUTTON = (By.CLASS_NAME, "CircleButton_type_next")
    PREV_BUTTON = (By.CLASS_NAME, "CircleButton_type_prev")
