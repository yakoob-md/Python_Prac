import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('stud.csv.csv')
s=df['gender']=='female'
print(s.value_counts())
groups=[A, B, C, D, 'E' ,'C']