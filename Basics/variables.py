import pandas as pd
import numpy as np
from scipy import stats
import math 
d=[200,600,100,50,900,450,500,600,380,250,670]
# mean
mean=np.mean(d)
print(mean,end='\n')
# sorting
print(np.sort(d))
# median
print(np.median(d))
# mode
print(stats.mode(d))
# variance 
print(np.var(d))
# SD
print(math.sqrt(np.var(d)))
# IQR
print(np.quantile(d,0.75)-np.quantile(d,0.25))
# Quartiles
print(np.quantile(d,[0,0.25,0.50,0.75,1]))
# Range
print(np.quantile(d,1)-np.quantile(d,0))
# CV
std=math.sqrt(np.var(d))
print(std/mean)
