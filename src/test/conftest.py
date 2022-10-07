import json
import os
import sys
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append(f'{os.path.dirname(os.path.abspath("main"))}')

print(os.path.dirname(os.path.abspath('..')))

@pytest.fixture(scope="class")
def driver_init(request):
    print("hello conftest")
    file = open(f"{os.path.dirname(os.path.abspath('tester'))}\preferences\setting.jsonp")
    url = json.load(file)
    file.close()
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get(url["_url"])

    return driver
    # request.cls.driver.quit()
    # yield
    # base.driver.quit()
