import pandas as pd

obj = pd.read_csv("Automobile_data.csv")
obj = obj.sort_values(by='price', ascending=False)
print("Highest Price of Company:",obj.head(1).company)