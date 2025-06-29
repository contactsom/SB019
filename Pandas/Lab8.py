import pandas as pd


sub_marks={"MATH":90,"PYTHON":89,"JAVA":78}
output=pd.Series(sub_marks,index=["Roll-1","Roll-2","Roll-3"])
print(output)
