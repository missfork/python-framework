import os
import sys
import allure


sys.path.append(f'{os.path.dirname(os.path.abspath("main"))}')
import time
from src.pages.login_page import LoginPage

#@allure.step("login into the page from test")
def test_login(driver_init):
    print("test_login page page")
    p = LoginPage(driver_init)
    p.login()
    time.sleep(10)
    allure.attach ('screenshot', driver_init.get_screenshot_as_png (), attachment_type=allure.attachment_type.PNG)
    print("test_login page end")
