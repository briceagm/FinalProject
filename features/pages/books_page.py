from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class BooksPage(BasePage):

    URL = 'https://librarius.md/ro/books'
    BOOKS_CATEGORIES_SELECTOR = (By.XPATH, '//li[@class="ac_item"]')
    ITEM_PER_PAGE_BUTTON_SELECTOR = (By.ID, 'perPageFilter')
    OPTION_WITH_16_BOOKS_SELECTOR = (By.XPATH, '//*[@id="perPageFilter"]/option[1]')
    OPTION_WITH_16_BOOKS_ON_PAGE_SELECTOR = (By.XPATH, '//div[@class="col-6 col-sm-4 col-md-6 col-lg-2 book-list"]')

    def get_books_categories_count(self):
        categories = self.driver.find_elements(*self.BOOKS_CATEGORIES_SELECTOR)
        return len(categories)

    def click_item_per_page_button(self):
        item_per_page_button = self.driver.find_element(*self.ITEM_PER_PAGE_BUTTON_SELECTOR)
        item_per_page_button.click()

    def click_option_with_16_books(self):
        option_with_16_books = self.driver.find_element(*self.OPTION_WITH_16_BOOKS_SELECTOR)
        option_with_16_books.click()

    def get_option_with_16_books_counter(self):
        option_with_16_books_on_page = self.driver.find_elements(*self.OPTION_WITH_16_BOOKS_ON_PAGE_SELECTOR)
        return len(option_with_16_books_on_page)