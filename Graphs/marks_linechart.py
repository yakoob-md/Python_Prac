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
plt.plot(n,maths,color='k',label='maths')
plt.plot(n,phy,color='y',label='phy')
plt.plot(n,chem,color='g',label='chem')
plt.plot(n,info,color='b',label='ip')
plt.legend()
plt.grid()
plt.show()
