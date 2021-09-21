#!/usr/bin/env python3

import os
import getpass
from datetime import datetime
import reports
import emails

user = getpass.getuser()
path = '/home/{}/'.format(user)
text_path = '/home/{}//supplier-data/descriptions/'.format(user)
files = os.listdir(text_path)

def main():
    date = datetime.now()
    month, day, year = date.strftime('%B'), date.strftime('%d'), date.strftime('%Y')
    title = "Processed Update on {} {}, {}".format(month, day, year)
    data = ''
    # puts data in format for uploading to the report using reports.py and then sends it to emails.py
    for file in files:
      with open(text_path + file, 'r') as opened:
          lines = opened.read().splitlines()
          if lines[-1] == '':
          	lines.pop()
          lines.pop(-1)
          name = True
          i = 0
          for line in lines:
              if name == True:
                data += 'Name: '
                name = False
              else:
                data += 'Weight: '
                name = True
              data += line + '<br/>'
              if name == True and i != 0:
                data += '<br/>'
              i += 1
    report = reports.generate_report(path + 'processed.pdf', title, data)
    sender = 'automation@example.com'
    reciever = '{}@example.com'.format(user)
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate_email(sender, reciever, subject, body, path + 'processed.pdf')
    emails.send_email(message)

if __name__ == "__main__":
	main()