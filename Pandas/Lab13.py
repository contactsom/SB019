import pandas as pd

data={
    "sub" :["MATH","PYTHON","JAVA"],
    "marks" :[90,89,78]
    }

output=pd.DataFrame(data,index=["Roll-1","Roll-2","Roll-3"])
print(output.loc["Roll-1"])
print(output.loc["Roll-2"])
print(output.loc["Roll-3"])
