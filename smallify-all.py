#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import os
from shutil import copyfile
import subprocess

source = 'smallify.bat'

# base_path = os.getcwd()
# bat_name = r"\smallify.bat"
# process = base_path + bat_name
# print(process)


previous_dir = os.getcwd()
for root, dirs, files in os.walk(".", topdown=True):
    for name in dirs:
        path = (os.path.join(root, name))
        print(path)
        target = os.path.join(path, source)
        try:
            print("copying : " + source + " into : " + target)
            copyfile(source, target)
        except Exception as e:
            # print(e)
            pass

for root, dirs, files in os.walk(".", topdown=True):
    for name in dirs:
        path = (os.path.join(root, name))
        try:
            os.chdir(path)
            subprocess.call(source)
            try:
                os.remove("smallify.bat")
            except:
                pass
            os.chdir(previous_dir)
        except Exception as e:
            # print(e)
            pass

input("Terminé\nPressez une touche pour quitter\n")
