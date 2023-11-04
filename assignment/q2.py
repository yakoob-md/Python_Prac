import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Olympic_medals.csv',encoding='ISO-8859-1')
df1=df[df['Country'].isin(['United States','United Kingdom','Canada'])&(df['Medal']=='Gold')]
print(df1["Medal"].value_counts())
