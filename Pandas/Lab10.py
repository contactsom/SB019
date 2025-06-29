import pandas as pd

data={
    "sub" :["MATH","PYTHON","JAVA"],
    "marks" :[90,89,78]
    }

output=pd.DataFrame(data)
print(output.loc[0])
print(output.loc[1])
print(output.loc[2])
