import os
import sys
import allure
import  pytest


from src.test.base_test import Base_Test

sys.path.append(f'{os.path.dirname(os.path.abspath("main"))}')
from src.pages.module import ModulePage
import time
from src.pages.login_page import LoginPage


class Test_Module(Base_Test):
    @pytest.mark.mod
    def test_module(self):
         print("test_login page page")
    
         log=LoginPage(self.driver)
         log.login()
         mod=ModulePage(self.driver)
         mod.module()
         mod.general_tab("sssssssssss")

         print("test_login page end")


    