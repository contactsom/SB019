import pandas as pd


df=pd.read_csv('mydata.csv')

print("*********BEFORE*******************")
print(df.to_string())
print("**********AFTER******************")
newdf=df.dropna()
print(newdf.to_string())


