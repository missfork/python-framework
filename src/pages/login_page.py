import sys
import os

import pytest
import  allure

# sys.path.append(f'{os.path.dirname(os.path.abspath("main"))}\\src\\pages')
from .base_page import Base


class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #@allure.step("login into the page from page")
    def login(self):
        print("login page start")
        self.element_input('input[placeholder="Email"]', "snape@gmail.com")
        self.element_input('input[placeholder="Password"]', 'Teacher@123')
        self.click('button[class="btn--pill mb-1 btn btn-primary btn-block"]')
        print("login page end")
