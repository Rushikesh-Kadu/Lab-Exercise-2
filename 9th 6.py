import pandas as pd

df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby('company')
print(car_Manufacturers[['company','average-mileage']].mean())
