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
    BASKET_BUTTON_SELECTOR = (By.CLASS_NAME, 'show-basket')
    DELETE_ICON_SELECTOR = (By.XPATH, "//i[@class='fa fa-trash']")
    CART_COUNTER_SELECTOR = (By.XPATH, '//span[@class="sb-footer-total-count"]')
    BOOKSTORE_BUTTON_SELECTOR = (By.XPATH, '//div[@class="top-bar-wrapper tb-darkgrey"]/a[4]')
    LOCATIONS_COUNT_SELECTOR = (By.XPATH, '//div[@class="shop-item list-group-item"]')
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

    def search_and_add_product_to_cart(self, book):
        self.click_search_box()
        self.input_name_of_the_book(book)
        self.click_search_button()
        self.click_book_title()
        self.click_add_to_cart_button()

    def click_basket_button(self):
        basket_button = self.driver.find_element(*self.BASKET_BUTTON_SELECTOR)
        basket_button.click()

    def click_delete_icon(self):
        delete_icon = self.driver.find_element(*self.DELETE_ICON_SELECTOR)
        delete_icon.click()

    def get_cart_counter(self):
        cart_counter = self.driver.find_element(*self.CART_COUNTER_SELECTOR)
        return cart_counter.text

    def click_bookstore_button(self):
        bookstore_button = self.driver.find_element(*self.BOOKSTORE_BUTTON_SELECTOR)
        bookstore_button.click()

    def get_locations_count(self):
        locations_count = self.driver.find_elements(*self.LOCATIONS_COUNT_SELECTOR)
        return len(locations_count)
