import smtplib, ssl
from email.mime.text import MIMEText
from datetime import datetime

from constants import sender_email, password, receiver_email, receiver_email1
port = 587

smtp_server = "smtp.gmail.com"
sender_email = sender_email
password = password
receiver_email = receiver_email


text = "day 1: Hi there This This is a message from Python." + datetime.today().strftime('%Y-%m-%d')
message = MIMEText(text, "plain")
message["subject"] = "Grevinge winter weather updates"
message["From"] = sender_email
message["To"] = receiver_email


context = ssl.create_default_context()

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email send successfully")
except Exception as e:
    print(f"Failed to send email: {e}")
'''
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email1, message)
    print("Email send successfully")
'''