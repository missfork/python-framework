import time
from .base_page import Base

class ModulePage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def module(self):
        self.click(self.css("library"))
        self.click(self.css("module"))
        time.sleep(1)
        self.click(self.css("createModule"))


    def general_tab(self,info):
        self.element_input(self.css("moduleName"),info)
        time.sleep(4)






    def css(self, key):
        return self.config_read('module.ini', 'css', key)
