import pandas as pd


a=[1,6,8]
output=pd.Series(a,index=["X","Y","Z"])
print(output)
print(output['X'])
print(output['Y'])
print(output['Z'])
