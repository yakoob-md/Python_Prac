import pandas as pd
import numpy as np
df=pd.read_csv("Olympic_medals.csv",encoding='ISO-8859-1')
print(df.shape)
# all years
df1=df[df['Country'].isin(['United States','Canada','United Kingdom'])&(df['Medal']=='Gold')]
print(df1['Gender'].value_counts())
# year 1976
df2=df1=df[df['Country'].isin(['United States','Canada','United Kingdom'])&(df['Medal']=='Gold')
&(df['Year']==2000)]
print(df2['Gender'].value_counts())
d=df['Discipline'].unique()
print(len(d))