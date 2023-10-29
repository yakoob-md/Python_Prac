import pandas as pd
import numpy as np
# creating df
i=['zone a','zone b','zone c','zone d']
s=pd.Series([56000,75000,70000,60000],i)
t=pd.Series([58000,68000,78000,61000],i)
dic={'sales':s,"target":t}
df=pd.DataFrame(dic)
print(df)
# adding a new col and a new row
df['orders']=[6000,7000,6800,5000]
df.at['zone e',:]=[50000,30000,np.NaN]
print(df)