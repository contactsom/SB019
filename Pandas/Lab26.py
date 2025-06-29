import pandas as pd


df=pd.read_csv('mydata.csv')
df.fillna({"Calories":130},inplace=True) # Because of Pandas version

print(df.to_string())



