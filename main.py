import os
import sys
#creating



def make_directory():
    print("script started-----------------------")
    dir=["config_files","preferences","test_suite","utilities","src","package"]
    for i in dir:
        print("----------------------------")
        print(i)
        print("_____________________________")
        cmd=os.popen(f"mkdir {i}")
        print(cmd.read())

    cmd\
        = os.popen(f"cd src")
    print(cmd.read())
    cmd =cmd=os.popen(f"mkdir tests")
    print(cmd.read())
    cmd =cmd=os.popen(f"mkdir pages")
    print(cmd.read())



print("sys" in sys.path)
make_directory()