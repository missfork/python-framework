import os
import sys
import allure
import  pytest

from src.test.base_test import Base_Test

sys.path.append(f'{os.path.dirname(os.path.abspath("main"))}')
import time
from src.pages.login_page import LoginPage


class Test_Login(Base_Test):
    @pytest.mark.login_1
    def test_login(self):
         print("test_login page page")
    
         p=LoginPage(self.driver)
         p.login()
         print("test_login page end")


    @pytest.mark.login_2
    def test_invalid_user_login(self):
        print("test_login page page")

        p = LoginPage(self.driver)
        p.invalid_username_login()
        print("test_login page end")

    @pytest.mark.login_3
    def test_invalid_password_login(self):
        print("test_login page page")

        p = LoginPage(self.driver)
        p.invalid_password_login()
        print("test_login page end")