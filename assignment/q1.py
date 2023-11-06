import pandas as pd
import numpy as np
df=pd.read_csv("Olympic_medals.csv",encoding='unicode-escape')
c=['United States','Canada','United Kingdom']
df1=df[df["Country"].isin(c)&(df['Medal']=="Gold")]
print(df1['Gender'].value_counts().sum())