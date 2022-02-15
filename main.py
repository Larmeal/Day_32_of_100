from calendar import weekday
import smtplib
import pandas
import random
import datetime as dt

now = dt.datetime.now()
week = now.weekday()

# if weekday == "1":
with open("quotes.txt") as quotes_file:
    read_quotes = quotes_file.readlines()
    random_quotes = random.choice(read_quotes)

with smtplib.SMTP("smtp.live.com") as connection:
    connection.starttls()
    connection.login(user="a1234@hotmail.com", password="123456")
    connection.sendmail(
        from_addr="a1234@hotmail.com", to_addrs="a5678@gmail.com", 
        msg=f"Subject:Monday motivation Python\n\n{random_quotes}"
    )
    connection.close()