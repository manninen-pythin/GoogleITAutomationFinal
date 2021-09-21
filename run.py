#!/usr/bin/python3

import requests
import os
import getpass

# {"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"} format

url = "http://localhost/fruits/"
user = getpass.getuser()
path = '/home/{}/supplier-data/descriptions/'.format(user)
files = os.listdir(path)

categories = ["name", "weight", "description"]
for file in files:
    with open(path + file, 'r') as opened:
        lines = opened.read().splitlines()
        data = {categories[i]: lines[i] for i in range(len(categories))}
        filename = file.split('.')
        data['image_name'] = filename[0] + '.jpeg'
        data['weight'] = int(data['weight'].rstrip(' lbs'))
        r = requests.post(url, json=data)