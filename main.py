import smtplib

import pandas as pd

import datetime as dt

import os



current_day = dt.date.today().strftime("%#d.%#m")
future_Date = (dt.datetime.today() + dt.timedelta(days=2)).strftime("%#d.%#m")

data = pd.read_csv("data/Book2.csv")

for index, row in data.iterrows():
    name, date = row["names"], str(row["dates"])
    if date == future_Date:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="011eyalm@shamir.school", password=os.environ.get("password"))
            connection.sendmail(to_addrs="eyal3208@gmail.com", from_addr="011eyalm@shamir.school", msg=f"Subject:Birthday\n\n{name} has a birthday in 2 days")

