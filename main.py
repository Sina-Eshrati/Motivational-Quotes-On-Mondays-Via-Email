import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()
weekday = now.weekday()

my_email = "sina_eshrati@yahoo.com"
my_password = "euolagjhjfqaiddm"

if weekday == 0:
    with open("quotes.txt", "r") as file:
        data = file.readlines()
        quotes_list = [line.strip() for line in data]
        quote = choice(quotes_list)

    with smtplib.SMTP_SSL("smtp.mail.yahoo.com") as connection:
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:motivational quote of the day\n\n{quote}")
