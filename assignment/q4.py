import pandas as pd
d=pd.read_csv('IPL Matches 2008-2020.csv')
df3=d[(d['venue']) and (d['toss_decision']=='bat')]
print(df3['venue'].value_counts())