import pandas as pd

import datetime as dt

future_Date = (dt.datetime.today() + dt.timedelta(days=2)).strftime("%#d.%#m")

data = pd.read_csv("data/Book2.csv")

for index, row in data.iterrows():
    name, date = row["names"], str(row["dates"])
    if date == future_Date:
        print(f"{name} has a birthday in 2 days")
