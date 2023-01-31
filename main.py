import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "YOUR EMAIL"
password = "YOUR APP PASSWORD"
letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthday_data = pd.read_csv("birthdays.csv")
today = dt.datetime.now()
is_birthday = (birthday_data["month"]==today.month) & (birthday_data["day"]==today.day)
if is_birthday.any() == True:
    for lab, row in birthday_data[is_birthday].iterrows():
        with open("letter_templates/"+random.choice(letter_templates), mode="r") as letter:
            letter_content = letter.read()
        
        recipient = row["name"].title()
        letter_content = letter_content.replace("[NAME]", recipient)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=row["email"], 
                msg=f"Subject:Happy Birthday\n\n{letter_content}")