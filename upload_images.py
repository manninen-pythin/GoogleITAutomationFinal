#!/usr/bin/python3

import os
import requests
import sys

# path of the data, and url of the site it is posted to
path = sys.argv[1]
url = sys.argv[2]

def get_data(file):
    # retrieves review data line by line and converts it to a dict
    dict_categories = ["title", "name", "date", "feedback"]
    i = 0
    review_data = dict()
    with open('/data/feedback/{}'.format(file), 'r') as f:
        for line in f.read().splitlines():
            review_data[dict_categories[i]] = line
            i += 1
    print(review_data)
    return review_data

def send_data(payload):
    r = requests.post(url, data=payload)
    if r.status_code >= 200 and r.status_code <= 299: 
        print('data sent successfully with status code ' + str(r.status_code))
    else:
        r.raise_for_status

def main():
    files = os.listdir(path)
    for file in files:
        payload = get_data(file)
        send_data(payload)
main()