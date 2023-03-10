import time

from behave import *


@Given("I am on the main page Librarius")
def step_impl(context):
    context.main_page.get_page()


@When("I click on the search box")
def step_impl(context):
    context.main_page.click_search_box()


@When('I input the name of the book "{book}"')
def step_impl(context, book):
    context.main_page.input_name_of_the_book(book)


@When("I click on the search button")
def step_impl(context):
    context.main_page.click_search_button()


@Then('I am on the page with the results and I found the book "Alchimistul"')
def step_impl(context):
    assert context.main_page.get_book_title() == 'Alchimistul'


@When('I click on the book "Alchimistul"')
def step_impl(context):
    context.main_page.click_book_title()


@When("I click on the add to cart button")
def step_impl(context):
    context.main_page.click_add_to_cart_button()


@Then("The cart button is incremented by one")
def step_impl(context):
    assert context.main_page.get_cart_badge_counter() == '1'


@When("I click books button")
def step_impl(context):
    context.main_page.click_books_button()


@Then("I am on the books page")
def step_impl(context):
    assert context.browser.get_current_url() == context.books_page.URL


@When('I add an product "{book}" to cart')
def step_impl(context, book):
    context.main_page.search_and_add_product_to_cart(book)


@When('I click the basket button')
def step_impl(context):
    context.main_page.click_basket_button()


@When('I click on the delete icon')
def step_impl(context):
    context.main_page.click_delete_icon()
    time.sleep(5)


@Then('The cart counter becomes 0')
def step_impl(context):
    assert context.main_page.get_cart_counter() == '0'


@When("I click the 'Librarii' button")
def step_impl(context):
    context.main_page.click_bookstore_button()


@Then("There are 47 locations of points of sales")
def step_impl(context):
    assert context.main_page.get_locations_count() == 47


@When("I click show sidebar and sidebar appears")
def step_impl(context):
    context.main_page.click_show_side_bar_button()


@When("I click on close sidebar button and sidebar is hidden")
def step_impl(context):
    context.main_page.click_close_bar_button()


@Then("I am on the main page Librarius")
def step_impl(context):
    assert context.browser.get_current_url() == context.main_page.URL