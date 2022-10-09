import json
import os
import shutil
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
allowed_extension = [".txt", ".json", ".properties"]
file_present = []
date_add = datetime.now()
folder_name = "report" + date_add.strftime("-%d-%m-%Y-%H-%M-%S")
report_folder = dir_path + "/allure"

count = 0


def search():
    global count
    for ext in os.listdir(report_folder):
        print(ext + "---" + folder_name)
        for i in allowed_extension:
            if ext.endswith(i):
                count = count + 1
                file_present.append(ext)
                break





def report_arrange():
    if len(file_present) == 5:
        os.mkdir(f'{report_folder}/{folder_name}')
        for i in file_present:
            shutil.move(f'{report_folder}/' + i, f'{report_folder}/{folder_name}/')


search()
report_arrange()
file_present.clear()
search()




