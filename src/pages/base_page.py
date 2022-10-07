import configparser
import time

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
            print(f'{e}  element_not_Found"')

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

    def config_read(self):
        self.config.read('./test.ini')
        print(self.config.get('css', 'msg'))

    def file_upload(self, css, file_path):
        self.locator(css).send_keys(file_path)
        if self.driver.page_source.find("File Uploaded!"):
            print("file upload success")
        else:
            print("file upload not successful")
