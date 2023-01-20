from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class LoginPage(BasePage):

    URL = 'https://www.librarius.md/'
    MY_ACCOUNT_BUTTON_SELECTOR = (By.XPATH, '//div[text()="Contul meu"]')
    USERNAME_SELECTOR = (By.ID, 'inputEmail')
    PASSWORD_SELECTOR = (By.ID, 'inputPassword')
    LOGIN_BUTTON_SELECTOR = (By.XPATH, '//button[@class="btn btn-success"]')
    USER_NAME_SELECTOR = (By.XPATH, "//a[text()='johndoe@gmail.com']")

    def click_my_account_button(self):
        account_button = self.driver.find_element(*self.MY_ACCOUNT_BUTTON_SELECTOR)
        account_button.click()

    def input_username(self, username):
        username_input = self.driver.find_element(*self.USERNAME_SELECTOR)
        username_input.send_keys(username)

    def input_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_SELECTOR)
        password_input.send_keys(password)


    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()


    def click_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()

    def find_user(self):
        user_name = self.driver.find_element(*self.USER_NAME_SELECTOR)
        return user_name.text