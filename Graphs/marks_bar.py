import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('marks.csv',index_col=0)
print(df)
names=df.loc[:,'name']
maths=df['maths']
phy=df['phy']
chem=df['chem']
info=df['info']
n=np.arange(len(names))
plt.bar(n,maths,label='maths',width=0.15)
plt.bar(n+0.15,maths,label='phy',width=0.15)
plt.bar(n+0.30,maths,label='chem',width=0.15)
plt.bar(n+0.45,maths,label='info',width=0.15)
plt.xticks(n,names)
plt.legend()
plt.grid()
plt.show()
# manual figure size 
plt.figure(figsize=(100,100))