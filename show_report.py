import os
import sys

def show_repot():
    cmd=os.popen("allure serve allure/")
    print(cmd.read())

def run_with_report():
    
    cmd=os.popen("pytest --alluredir=allure/")
    print(cmd.read())


#how_repot()

run_with_report()

print("_____________________________")
