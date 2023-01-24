from behave import *


@Given("I am on the books page")
def step_impl(context):
    context.books_page.get_page()


@When("I found the books menu")
def step_impl(context):
    pass


@Then("There are 11 categories of the books on the menu")
def step_impl(context):
    assert context.books_page.get_books_categories_count() == 11


@When("I click the drop and down button 'page filter'")
def step_impl(context):
    context.books_page.click_item_per_page_button()


@When("I pick the number 16 from the list")
def step_impl(context):
    context.books_page.click_option_with_16_books()


@Then("There are 16 books on the page")
def step_impl(context):
    assert context.books_page.get_option_with_16_books_counter() == 16


@When("I click the drop and down button 'by filter'")
def step_impl(context):
    context.books_page.click_sort_books_by_filter()


@When("I pick the option with ascending price")
def step_impl(context):
    context.books_page.click_price_ascending_button()


@Then("There are books ordered ascending on the page")
def step_impl(context):
    pass
    # assert context.browser.get_current_url() == context.books_page.URL


@When("I click on the logo 'Librarius' button")
def step_impl(context):
    context.books_page.click_logo_button()


@Then("I am on the main page")
def step_impl(context):
    assert context.browser.get_current_url() == context.main_page.URL