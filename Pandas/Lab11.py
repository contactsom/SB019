import pandas as pd

data={
    "sub" :["MATH","PYTHON","JAVA"],
    "marks" :[90,89,78]
    }

output=pd.DataFrame(data)
print(output.loc[[0,1,2]])
