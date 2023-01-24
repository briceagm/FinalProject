from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class BooksPage(BasePage):

    URL = 'https://librarius.md/ro/books'
    BOOKS_CATEGORIES_SELECTOR = (By.XPATH, '//li[@class="ac_item"]')
    ITEMS_ON_PAGE_BUTTON_SELECTOR = (By.ID, 'perPageFilter')
    OPTION_WITH_16_BOOKS_SELECTOR = (By.XPATH, '//*[@id="perPageFilter"]/option[1]')
    COUNT_16_BOOKS_ON_PAGE_SELECTOR = (By.XPATH, '//div[@class="col-6 col-sm-4 col-md-6 col-lg-2 book-list"]')
    SORT_BOOKS_BUTTON_SELECTOR = (By.ID, 'sortByFilter')
    PRICE_ASCENDING_BUTTON_SELECTOR = (By.XPATH, '//*[@id="sortByFilter"]/option[3]')
    LOGO_BUTTON_SELECTOR = (By.CLASS_NAME, 'header-logo-text')
    def get_books_categories_count(self):
        categories = self.driver.find_elements(*self.BOOKS_CATEGORIES_SELECTOR)
        return len(categories)

    def click_item_per_page_button(self):
        item_per_page_button = self.driver.find_element(*self.ITEMS_ON_PAGE_BUTTON_SELECTOR)
        item_per_page_button.click()

    def click_option_with_16_books(self):
        option_with_16_books = self.driver.find_element(*self.OPTION_WITH_16_BOOKS_SELECTOR)
        option_with_16_books.click()

    def get_option_with_16_books_counter(self):
        count_16_books_on_page = self.driver.find_elements(*self.COUNT_16_BOOKS_ON_PAGE_SELECTOR)
        return len(count_16_books_on_page)

    def click_sort_books_by_filter(self):
        sort_books_by_filter = self.driver.find_element(*self.SORT_BOOKS_BUTTON_SELECTOR)
        sort_books_by_filter.click()

    def click_price_ascending_button(self):
        price_ascending_button = self.driver.find_element(*self.PRICE_ASCENDING_BUTTON_SELECTOR)
        price_ascending_button.click()

    def click_logo_button(self):
        logo_button = self.driver.find_element(*self.LOGO_BUTTON_SELECTOR)
        logo_button.click()
