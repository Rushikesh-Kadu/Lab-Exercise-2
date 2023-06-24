import pandas as pd

GermanCars={'company':['Ford','Mercedes','BMv','Audi'],'Price': [23845, 171995, 135925 ,71400]}
carsdf1=pd.DataFrame.from_dict(GermanCars)
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500, 58900]}
carsdf2=pd.DataFrame.from_dict(japaneseCars)
carsdf=pd.concat([carsdf1,carsdf2],keys=["Germany","Japan"])
print(carsdf)