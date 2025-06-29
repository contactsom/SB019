import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('mydata1.csv',sep='\s+')

df.columns=df.columns.str.strip() # Remove the extra white space in the column


# Remove the single quote from the 'date' column
df['Date']= df['Date'].astype(str).str.replace("'","",regex=False)
df['Date']=pd.to_datetime(df['Date'],errors='coerce')

df.dropna(subset=['Date'],inplace=True)
df.loc[7,'Duration']=45

#print("Is Duplicate",df.duplicated()) # 12     True

df.drop_duplicates(inplace=True)

print("Is Null",df.isnull()) # 12     True

df.plot()
plt.show()

print(df.to_string())





