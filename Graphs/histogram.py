import pandas as pd
import matplotlib.pyplot as plt
# for histogram
# three parameters - data bins and width
# optional linestyle and edge color and colors
ages=[12,23,2,18,23,20,30,36,27,38,5,36,27,28,27,8,23,45,56,78
      ,34,56,23,45,67,4,43,22,23,34,55,66,78,10]
plt.hist(ages,bins=5,linestyle='dashed',edgecolor='r',color='g')
plt.show()