from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class MainPage(BasePage):

    URL = 'https://librarius.md/ro/'
    SEARCH_BOX_SELECTOR = (By.ID, 'searchbox')
    SEARCH_BUTTON_SELECTOR = (By.XPATH, '//*[@id="autocomplete-box"]/div/button')
    BOOK_TITLE_SELECTOR = (By.CLASS_NAME, 'card-title')
    ADD_TO_CART_BUTTON_SELECTOR = (By.ID, 'addToCartButton')
    CART_BADGE_SELECTOR = (By.XPATH, '//*[@id="header-cart-count-badge"]/b')
    BOOKS_BUTTON_SELECTOR = (By.XPATH, '//*[@id="topmenu"]/div/a[2]/span')

    def click_search_box(self):
        search_box = self.driver.find_element(*self.SEARCH_BOX_SELECTOR)
        search_box.click()

    def input_name_of_the_book(self, book):
        search_box = self.driver.find_element(*self.SEARCH_BOX_SELECTOR)
        search_box.send_keys(book)

    def click_search_button(self):
        search_button = self.driver.find_element(*self.SEARCH_BUTTON_SELECTOR)
        search_button.click()

    def get_book_title(self):
        book_title = self.driver.find_element(*self.BOOK_TITLE_SELECTOR)
        return book_title.text

    def click_book_title(self):
        book_title = self.driver.find_element(*self.BOOK_TITLE_SELECTOR)
        book_title.click()

    def click_add_to_cart_button(self):
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_BUTTON_SELECTOR)
        add_to_cart_button.click()

    def get_cart_badge_counter(self):
        cart_badge_counter = self.driver.find_element(*self.CART_BADGE_SELECTOR)
        return cart_badge_counter.text

    def click_books_button(self):
        books_button = self.driver.find_element(*self.BOOKS_BUTTON_SELECTOR)
        books_button.click()