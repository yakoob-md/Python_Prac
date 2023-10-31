import pandas as pd
import numpy as np
import scipy.stats as sts
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
print(sts.mode(d))
