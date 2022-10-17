import os
import sys


def run_with_report():
    cmd = os.popen("pytest --alluredir=allure/")
    print(cmd.read())


run_with_report()

print("_____________________________")
