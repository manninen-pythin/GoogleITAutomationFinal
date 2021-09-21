#!/usr/bin/env python3
import requests
import os
import getpass

url = "http://localhost/upload/"
user = getpass.getuser()
path = '/home/{}/supplier-data/images/'.format(user)
files = os.listdir(path)

for file in files:
    with open(path + file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})