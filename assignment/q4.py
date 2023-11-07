import pandas as pd
df=pd.read_csv('IPL Matches 2008-2020.csv')
df3=df[(df['toss_decision']=='bat')]
print(df3['venue'].value_counts().max())
print(df3.iloc[0:1,"venue"])