import json

import os
import sys
import time
from datetime import datetime

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append(f'{os.path.dirname(os.path.abspath("main"))}')

print(os.path.dirname(os.path.abspath('..')))

from src.pages.base_page import Base


@pytest.fixture(scope="function")
def driver_init(request):
    # global driver
    # print("--confest start--")
    print("-----run----")
    file = open(f"{os.path.dirname(os.path.abspath('report.py'))}/preferences/setting.json")
    url = json.load(file)
    file.close()
    options = Options()

    # """Sets chrome options for Selenium.
    # Chrome options for headless browser is enabled.
    # """

    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # chrome_prefs = {}
    # options.experimental_options["prefs"] = chrome_prefs
    # chrome_prefs["profile.default_content_settings"] = {"images": 2}

    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

    driver.maximize_window()

    driver.get(url["_url"])
    request.cls.driver = driver
    yield driver
    print("end")

    final_snap(driver)
    driver.quit()


def final_snap(driver):
    date_add = datetime.now()
    dir_path = os.path.dirname(os.path.realpath("report.py"))
    dateTimeNow = date_add.strftime("-%d-%m-%Y-%H-%M-%S")
    name = f"{dir_path}/screen_shot/snap{dateTimeNow}.png"
    driver.save_screenshot(name)
    allure.attach.file(name, f'final{dateTimeNow}',
                       attachment_type=allure.attachment_type.PNG)
