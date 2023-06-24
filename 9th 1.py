import pandas as pd

obj = pd.read_csv('Automobile_data.csv')
print("First 5 Rows:")
print(obj.head(5))
print("Last 5 Rows:")
print(obj.tail(5))