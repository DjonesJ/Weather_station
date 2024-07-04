import smtplib, ssl
from constants import sender_email, password, receiver_email, receiver_email1
port = 587

smtp_server = "smtp.gmail.com"
sender_email = sender_email
password = password
receiver_email = receiver_email


message = "Subject: Hi there This This is a message from Python. \
    Body: This is a test"

context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("Email send successfully")
'''
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email1, message)
    print("Email send successfully")
'''