import pandas as pd
# first df
df1=pd.read_csv("Book 1.csv",index_col=0)
print(df1)
print()
# second df
i=['zone a','zone b','zone c','zone d']
s=pd.Series([56000,75000,70000,60000],i)
t=pd.Series([58000,68000,78000,61000],i)
dic={'sales':s,"target":t}
df2=pd.DataFrame(dic)
print(df2)
# appending 
df3=df1.append(df2,ignore_index=True)
# ignore index for continuous row index 
print(df3)
