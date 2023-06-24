import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 ,71400]}
carpricedf=pd.DataFrame.from_dict(Car_Price)
Car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 ,160]}
carhorsepowerdf=pd.DataFrame.from_dict(Car_Horsepower)
carsdf=pd.merge(carpricedf,carhorsepowerdf,on='Company')
print(carsdf)