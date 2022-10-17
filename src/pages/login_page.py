import sys
import os
import time

import pytest
import allure

# sys.path.append(f'{os.path.dirname(os.path.abspath("main"))}\\src\\pages')
from .base_page import Base


class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # @allure.step("login into the page from page")
    def login(self):
        self.element_input(self.css('email'), "snape@gmail.com")
        self.element_input(self.css('password'), 'Teacher@123')
        self.click(self.css('login_button'))

        logout = self.locator(self.css('logout_button')).text.replace(" ", "").lower()

        print(f"----------{logout}----------------")

        assert logout == 'logout'

    def css(self, key):
        return self.config_read('login.ini', 'css', key)

    def invalid_username_login(self):
        self.element_input(self.css('email'), "snape@invalid.com")
        self.element_input(self.css('password'), 'Teacher@123')
        self.click(self.css('login_button'))
        time.sleep(1)

        print(f"actual {self.css('actual_url')}")
        print(f"current {self.driver.current_url}")

        assert self.css('actual_url') == self.driver.current_url

    def invalid_password_login(self):
        self.element_input(self.css('email'), "snape@gmai.com")
        self.element_input(self.css('password'), 'invalid_password')
        self.click(self.css('login_button'))
        time.sleep(1)
        print(f"actual {self.css('actual_url')}")
        print(f"current {self.driver.current_url}")
        assert self.css('actual_url') == self.driver.current_url

    def css(self, key):
        return self.config_read('login.ini', 'css', key)
