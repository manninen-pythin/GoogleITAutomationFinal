#!/usr/bin/python3

import psutil
import emails
import getpass
import socket


def check_stats():
    percent = psutil.cpu_percent(interval=1)
    usage = psutil.disk_usage('/')
    memory = psutil.virtual_memory()
    threshold = 500 * 1024 * 1024 # 500MB
    if percent > 80.0:
        return "Error - CPU usage is over 80%"
    if usage[3] > 80.0:
        return "Error - Available disk space is less than 20%"
    if memory.percent < threshold:
        return "Error - Available memory is less than 500MB"
    try:
        resolve = socket.gethostbyname()
        if resolve != '127.0.0.1':
            return "Error - localhost cannot be resolved to 127.0.0.1"
    except socket.error:
        return "Error - localhost cannot be resolved to 127.0.0.1"
    return 'all clear'

def send_alert(error_message):
    user = getpass.getuser()
    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(user)
    subject = error_message
    body = 'Please check your system and resolve the issue as soon as possible.'
    message = emails.generate_email(sender, recipient, subject, body, None)
    emails.send_email(message)


def main():
    error = check_stats()
    if error != "all clear":
        send_alert(error)
main()