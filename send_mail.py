#!/usr/bin/python3

from email.message import EmailMessage
import mimetypes
import os
import smtplib
import getpass

def new_message(sender, recipient, subject):
    # creates email to be sent and returns it
    message = EmailMessage()

    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject

    body = input('Enter body text: ')

    message.set_content(body)

    return message

def add_attachment(message):
    # adds attachment if necessary

    attachment_path = "/tmp/example.png"
    attachment_filename = os.path.basename(attachment_path)
    mime_type = mimetypes.guess_type(attachment_path)
    print(mime_type)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))
    return message

def send_message(sender, message):
    # connects and authenticates to the smtp server and sends newly created email to recipient
    mail_server = smtplib.SMTP('localhost')
    # SSL version: mail_server = smtplib.SMTP_SSL('smtp.example.com')
    password = getpass.getpass('Enter passord: ')
    # need  to make the sender variable global or pass to function
    mail_server.login(sender, mail_pass)
    mail_server.send_message(message)
    mail_server.quit()

def main():
    sender = input("Enter sender's email address: ")
    recipient = input("Enter recipient's email address: ")
    subject = input("Enter subject: ")
    message = new_message(sender, recipient, subject)
    attachments = input('Does the email have any attachments? Y or N')
    if attachments == 'Y' or attachments == 'y':
        message = add_attachment(message)
    send_message(sender, message)
main()