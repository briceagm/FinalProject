from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class LoginPage(BasePage):

    URL = 'https://www.librarius.md/'
    MY_ACCOUNT_BUTTON_SELECTOR = (By.XPATH, '//div[text()="Contul meu"]')
    USERNAME_SELECTOR = (By.ID, 'inputEmail')
    PASSWORD_SELECTOR = (By.ID, 'inputPassword')
    LOGIN_BUTTON_SELECTOR = (By.XPATH, '//button[@class="btn btn-success"]')
    USER_NAME_SELECTOR = (By.XPATH, "//a[text()='johndoe@gmail.com']")
    ERROR_MSG_SELECTOR = (By.XPATH, '//p[@class="bg-danger"]')
    LOGOUT_BUTTON_SELECTOR = (By.XPATH, '//a[@href="https://librarius.md/ro/logout"]')
    CAROUSEL_SELECTOR = (By.XPATH, '//li[@data-target="#carouselExampleIndicators"]')

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
        self.click_my_account_button()
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()

    def click_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()

    def find_user(self):
        user_name = self.driver.find_element(*self.USER_NAME_SELECTOR)
        return user_name.text

    def get_error_msg(self):
        error_message_box = self.driver.find_element(*self.ERROR_MSG_SELECTOR)
        return error_message_box.text

    def click_logout_button(self):
        logout_button = self.driver.find_element(*self.LOGOUT_BUTTON_SELECTOR)
        logout_button.click()
