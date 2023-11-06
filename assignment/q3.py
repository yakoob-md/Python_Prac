import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('stud.csv.csv')
df1=df[df['gender']=='female']
print(df1.value_counts().sum())