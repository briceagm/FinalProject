from features.browser import Browser
from features.pages.login_page import LoginPage
from features.pages.main_page import MainPage
from features.pages.books_page import BooksPage

def before_scenario(context, scenario):
    context.browser = Browser()
    context.login_page = LoginPage(context.browser)
    context.main_page = MainPage(context.browser)
    context.books_page = BooksPage(context.browser)

def after_scenario(context, scenario):
    context.browser.quit()
