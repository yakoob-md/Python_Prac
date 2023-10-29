import pandas as pd
import numpy as np
i=[1,2,3,4,5]
s=pd.Series(['artha','priya','neil','kein','arjun'],i)
d=pd.Series(['f','f','m','m','m'],i)
e=pd.Series([20,40,45,35,48],i)
dic={'names':s,"sex":d,'marks':e}
df=pd.DataFrame(dic)
print(df)
df.to_csv('Book 1.csv')
print('done')
