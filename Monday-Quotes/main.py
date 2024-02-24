import smtplib
from datetime import datetime
import random
import json

with open('../config.json') as f:
    config_data = json.load(f)

# Access database configuration
smtp_server = config_data['email']['host']
smtp_port = config_data['email']['port']
SENDER = config_data['email']['sender']
RECEIVER = config_data['email']['receiver']
PASSWORD = config_data['email']['password']


def send_email(sender, receiver, message):
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=sender, password=PASSWORD)
        connection.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=message)


def read_file(file_name):
    with open(file_name) as file:
        list_of_content = file.readlines()
    return list_of_content


now = datetime.now()
if now.weekday() == 5:
    quote_list = read_file("quotes.txt")
    random_quote = random.choice(quote_list)
    email_message = f"""Subject: Daily Quote\n\n
    {random_quote}"""
    print(email_message)
    send_email(SENDER, RECEIVER, email_message)

# print(now.weekday())
#
# date_of_birth = datetime(year=1989, month=9, day=18)
# print(date_of_birth)
