import pandas as pd
import numpy as np
df=pd.read_csv("Olympic_medals.csv",encoding='unicode-escape')
c=['United States','Canada','United Kingdom']
# a
df1=df[df["Country"].isin(c)&(df['Medal']=="Gold")]
print(df1['Gender'].value_counts().sum())
# b 
df2=df[df['Country'].isin(c)&(df['Medal']=="Gold")&(df['Year']==1976)]
print(df2["Gender"].value_counts())
# c
df3=df[df['Country'].isin(c)&(df['Medal']=="Gold")&(df['Year']==2000)]
print(df3["Gender"].value_counts().sum())
