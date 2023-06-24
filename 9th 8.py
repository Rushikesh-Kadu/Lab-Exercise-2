import pandas as pd

df=pd.read_csv("Automobile_data.csv")
car_manufacturers=df.groupby("company")
mileagedf=car_manufacturers[['company','average-mileage']].mean()
print(mileagedf.rank())