import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
aus=[80,59,59,198] 
eng=[45,45,46,136] 
can=[26,20,26,66]
medal=['gold','silver','bronze','total']
mtype=['gold','silver','bronze','total']
xpoints=np.arange(0,len(mtype))  
plt.bar(xpoints,aus,label="Australia",color='b',width=0.25)
plt.bar(xpoints+0.25,eng,label="England",color="r",width=0.25)
plt.bar(xpoints+0.50,can,label="Canada",color='orange',width=0.25)
plt.xticks(xpoints,mtype)
plt.legend()
plt.grid()
plt.show()
