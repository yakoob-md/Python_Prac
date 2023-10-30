import pandas as pd
import matplotlib.pyplot as plt
a=['BLR','DEL','CHN','KOL']
b=[190000,200000,150000,60000]
# there are two colors so it would appl alternate
# same will not apply to width 
# 4 bars means 4 widths should be thr or nil
plt.bar(a,b,width=[0.6,0.4,0.2,1.5],color=['r','y','g','k'])
plt.xlabel('City')
plt.ylabel("data")
plt.xticks(a,['a','b','c','d'])
plt.legend()
plt.grid()
plt.show()