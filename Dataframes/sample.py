import pandas as pd
import numpy as np
df=pd.read_csv('fds.csv',index_col=0)
print(df)
print()
df=pd.read_csv('fds.csv',index_col=0,usecols=['name','sec'])
print(df)