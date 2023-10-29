import pandas as pd
df=pd.read_csv("Book 1.csv",index_col=0)
print(df)
print()
# works with both positional and labelled 
# but positional only when indices are non numeric
print(df.sex[4])
print()
# at
# only labelled index 
print(df.at[2,"marks"]) 
print()
print(df.at[2,'sex'])
print()
print(df.iat[2,0])