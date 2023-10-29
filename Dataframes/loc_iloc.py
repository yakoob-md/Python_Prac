import pandas as pd
df=pd.read_csv("Book 1.csv",index_col=0)
print(df)
print()
# loc is or only laelled 
# whether the indeices are numbers or not 
print(df.loc[2:4,:]) 
print(df.loc[2:4,:])
print()
# both these would give the same output
# random rows then use double box brackets
print(df.loc[[2,5]])
print()
# in iloc positional index is used 
# whether index is numeric or not 
# the last provided index will not be retrieved 
print(df.iloc[1:3,:])
print()
# random rows then use double brackets
print(df.iloc[[1,4]])
print()
