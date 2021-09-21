#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Created on Mon Aug 30 08:26:58 2021

#@author: EricManninen

from PIL import Image
import os
import shutil
import getpass
import sys

user = getpass.getuser()
path = '/home/{}'.format(user) + str(sys.argv[1]) + '/'
new_path = '/home/{}'.format(user) + str(sys.argv[2]) + '/'
files = os.listdir(path)

def resize(image, length, width):
    # resizes and returns the image, returns exception if rotation fails
    try:
        image = image.resize((length, width))
        print('resized file')
        return image
    except Exception as e:
        print(e)

def format(file, image, f):
    # formats and saves the image, returns exception if saving and conversion fails
    try:
        print(new_path + file)
        image.convert("RGB").save(new_path + file.split('.')[0] + '.' + f,  "{}".format(f).upper(), quality=100)
        print("file converted and saved")
        os.remove(path + file)
    except Exception as e:
        print(e)

def main():
    f = 'jpeg'
    length, width = 600, 400
    for file in files:
        if '.' in file:
          print("modifying " + file)
          image = Image.open(path + file)
          image = resize(image, length, width)
          format(file, image, f)
        else:
            os.remove(path + file)
main()