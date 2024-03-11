import pandas as pd

import datetime as dt

future_Date = (dt.datetime.today() + dt.timedelta(days=2)).strftime("%#d.%#m")

data = pd.read_csv("data/Birthdays.csv")

msg = "יש יום הולדת עוד יומיים"

for index, row in data.iterrows():
    name, date = row["names"], str(row["dates"])
    if date == future_Date:
        print(f"ל{name} {msg}")
