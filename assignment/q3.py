import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('stud.csv.csv')
# a
df1=df[df['gender']=='female']
print(df1.value_counts().sum())
# b
g=['group A', 'group B', 'group C', 'group D' ,'group E' ,'group C']
df2=df[df['race/ethnicity'].isin(g)&(df['gender']=='male')]
print(df2.value_counts().sum())
# c
df3=df[(df['lunch']=='standard')&(df['gender']=='female')]
print(df3.value_counts().sum())
# e
df4=df[(df['reading score']>70) &(df['gender']=='male')]
print(df4.value_counts().sum())
# f
df5=df[(df['writing score']<70) &(df['gender']=='female')]
print(df5.value_counts().sum())
