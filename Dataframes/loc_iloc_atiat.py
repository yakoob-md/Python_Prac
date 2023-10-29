import pandas as pd
df=pd.read_csv("Book 1.csv",index_col=0)
print(df)
print()
print(df.loc['2':'4',:])