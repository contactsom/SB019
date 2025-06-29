import pandas as pd


df=pd.read_csv('mydata1.csv',sep='\s+')

df.columns=df.columns.str.strip() # Remove the extra white space in the column


# Remove the single quote from the 'date' column
df['Date']= df['Date'].astype(str).str.replace("'","",regex=False)
df['Date']=pd.to_datetime(df['Date'],errors='coerce')
print(df.to_string())



