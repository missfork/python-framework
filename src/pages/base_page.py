import configparser
import os
import time
from datetime import datetime

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def sleep(t):
    time.sleep(t)


class Base:

    def __init__(self, driver):
        self.driver = driver

        self.config = configparser.ConfigParser()
        self.wait = WebDriverWait

    def start(self):
        self.driver.get("https://release.ilearningengines.com/")
        self.driver.maximize_window()

    def wait_method(self, css):
        try:
            print("inside wait")
            self.wait(self.driver, 25).until(ec.presence_of_element_located((By.CSS_SELECTOR, css)))
            print("outside wait")
        except Exception as e:
            print(f'{e}  element_not_Found ')
            snap_name = f"failed_snap{self.dateTimeNow()}"
            self.snap_to_report(snap_name)

    def locator(self, css):
        self.wait_method(css)
        element = self.driver.find_element(By.CSS_SELECTOR, css)
        return element

        # To input element

    def element_input(self, css, name):
        self.locator(css).send_keys(name)

        # To click element

    def click(self, css):
        self.locator(css).click()

    def config_read(self, path, type, key):
        try:
            self.config.read(f"{os.path.dirname(os.path.realpath('main.py'))}/config_files/{path}")
            return self.config.get(type, key)
        except Exception as e:
            print(e)

    def dateTimeNow(self):
        date_add = datetime.now()
        return date_add.strftime("-%d-%m-%Y-%H-%M-%S")

    def get_text(self,css):
        return self.locator(css).text



    def file_upload(self, css, file_path):
        self.locator(css).send_keys(file_path)
        if self.driver.page_source.find("File Uploaded!"):
            print("file upload success")
        else:
            print("file upload not successful")

    def snap(self):

        dir_path = os.path.dirname(os.path.realpath("report.py"))
        name = f"{dir_path}/screen_shot/snap{self.dateTimeNow()}.png"
        self.driver.save_screenshot(name)
        print("snap")
        return name

    def snap_to_report(self, file_name):
        name = self.snap()
        allure.attach.file(name, file_name, attachment_type=allure.attachment_type.PNG)
