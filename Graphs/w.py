import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a=[1,2,3,4] 
b=[1,5,3,6] 
c=[7,2,5,3]
plt.plot(a,b,label='me',color='green',linestyle='dashed')
plt.plot(a,c,label='you',color='red',linestyle='dashed',marker='*',
         markersize=24,markerfacecolor='k',markeredgecolor='red')
plt.legend(loc='upper left')
plt.xlabel("data")
plt.ylabel("points")
plt.grid()
plt.show()
