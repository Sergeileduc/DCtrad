#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import os
from shutil import copyfile
import subprocess

source = 'smallify.bat'

small_tag = "\Smaller_comics"

# base_path = os.getcwd()
# bat_name = r"\smallify.bat"
# process = base_path + bat_name
# print(process)


previous_dir = os.getcwd()
primary_folder = ""
primary_foler_flag = False
for root, dirs, files in os.walk(".", topdown=True):
    for name in dirs:
        if not primary_foler_flag:
            primary_folder = name
            primary_foler_flag = True
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
                print("Launching smallify.bat in " + path)
                os.remove("smallify.bat")
            except:
                pass
            os.chdir(previous_dir)
        except Exception as e:
            # print(e)
            pass

try:
     os.chdir(previous_dir)
except:
    pass

smallified_folder = primary_folder + "_Smallified"

# Move smallified files
print("Moving file")
for root, dirs, files in os.walk(primary_folder, topdown=True):
    for name in files:
        source = (os.path.join(root, name))
        if small_tag in root:
            print("root : " + root)
            print("source : " + source)
            target_folder = root.replace(small_tag, '').replace(primary_folder, smallified_folder)
            target = os.path.join(target_folder, name)
            print("target : " + target_folder)
            try:
                os.makedirs(target_folder)
            except FileExistsError:
                pass
            try:
                os.rename(source,target)
            except Exception as e:
                print(e)

# Clean. Supprime les dossiers "Smaller_comics"
print("Cleaning")
for root, dirs, files in os.walk(primary_folder, topdown=True):
    for name in dirs:
        dir = (os.path.join(root, name))
        # if small_tag in root:
        print(dir)
        print(name)
        if name in small_tag:
            os.rmdir(dir)

# print(smallified_folder)
# os.mkdir(smallified_folder)

input("Terminé\nPressez une touche pour quitter\n")
