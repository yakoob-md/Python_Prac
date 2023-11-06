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