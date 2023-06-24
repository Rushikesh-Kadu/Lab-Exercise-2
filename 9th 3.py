import pandas as pd

df = pd.read_csv("Automobile_data.csv")
car_Man = df.groupby('company')
obj = car_Man.get_group('toyota')
print(obj)