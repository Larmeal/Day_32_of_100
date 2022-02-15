##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import random
import pandas
import datetime as dt

random_letter = random.randint(1, 3)

read_birthday = pandas.read_csv("birthday-wisher-extrahard-start/birthdays.csv")

day = dt.datetime.now()
today_now = (day.month, day.day)

birth_day = {(row.month, row.day) for (index, row) in read_birthday.iterrows()}
name_birth_day = {row.name for (index, row) in read_birthday.iterrows()}
letter_birthday = (f"birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1, 3)}.txt", "a")


if today_now in birth_day:
    with open(letter_birthday) as birthday_blessing:
        read = birthday_blessing.read()
        read.replace("[NAME]", name_birth_day)

    with smtplib.SMTP("smtp.live.com") as connection:
        connection.starttls()
        connection.login(user="a1234@hotmail.com", password="123456")
        connection.sendmail(
            from_addr="a1234@hotmail.com", 
            to_addrs="a5678@gmail.com", 
            msg=f"Subject:Happy Birth's Day\n\n{read}"
        )
        connection.close()

