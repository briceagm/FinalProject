from behave import *


@Given("I am on the main page")
def step_imp(context):
    context.login_page.get_page()


@When('I click the "Contul meu" button')
def step_imp(context):
    context.login_page.click_my_account_button()


@When('I input a "{username}" username')
def step_imp(context, username):
    context.login_page.input_username(username)


@When('I input a "{password}" password')
def step_imp(context, password):
    context.login_page.input_password(password)


@When("I click the login button")
def step_imp(context):
    context.login_page.click_login_button()


@Then("I find the username on the main page")
def step_imp(context):
    assert context.login_page.find_user() == 'johndoe@gmail.com'


@Then("I receive the error message")
def step_impl(context):
    expected_err_message = 'Numele de utilizator sau parola incorectă'
    assert context.login_page.get_error_msg() == expected_err_message