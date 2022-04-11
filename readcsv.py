import csv
import pandas as pd


file = 'data-files/airbnb_clean.csv'
data = pd.read_csv(file)


print(list(data.columns))
