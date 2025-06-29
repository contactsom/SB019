import pandas as pd


df=pd.read_csv('mydata.csv')

df.dropna(inplace=True)
# If you want to change the original Dataframe , then use the inplace=True

print(df.to_string())



