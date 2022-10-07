import configparser
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Base:
    def __init__(self):
        sys.path.append("D:/python_automation")
        options = Options()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.config = configparser.ConfigParser()
        print(os.getcwd())
        # json_file = open('setting.json')
        # setting = json.load(json_file)
        # json_file.close()
        #self.setting = setting



    def start(self):
        print("fixture-started")
        self.driver.get("https://release.ilearningengines.com/")
        self.driver.maximize_window()


    # used to wait until element found
    def wait_method(self, css):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
        except:
            print("element_not_Found")

    def locator(self, css):
        self.wait_method(css)
        return self.driver.find_element(By.CSS_SELECTOR, css)

    # To input element
    def element_input(self, css, name):
        self.locator(css).send_keys(name)

    # To click element
    def element_click(self, css):
        self.locator(css).click()

    def config_read(self):
        self.config.read('./test.ini')
        print(self.config.get('css', 'msg'))

    def file_upload(self, css, file_path):
        self.locator(css).send_keys(file_path)
        if self.driver.page_source.find("File Uploaded!"):
            print("file upload success")
        else:
            print("file upload not successful")



