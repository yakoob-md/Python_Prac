import pandas as pd
df=pd.read_csv("Book 1.csv",index_col=0)
print(df)
print()
print(df['names'])
print()
print(df.names)
print()
print(df[['names','sex']])
print()
# print(df["a":"c"])
print()
# 3 index will not be considered 
# even if the row index is numeric 
# it will consider the positional indexing only 
# df will slice for both labelled and positional index 
# but labelled only when they are non numeric
print(df['1':'3'])
print()
# only one row 
print(df[1:2])
print()
