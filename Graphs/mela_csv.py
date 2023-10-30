import pandas as pd
import matplotlib.pyplot as plt
w1=pd.Series([5000,5900,6500,3500,4000,5300,7900])
w2=pd.Series([4000,3000,5000,5500,3000,4300,5900])
w3=pd.Series([4000,5800,3500,2500,3000,5300,6000])
dic={"week 1":w1,"week 2":w2,"week 3":w3}
df=pd.DataFrame(dic)
print(df)
df.plot(kind='line',color=['red','green','b'],linestyle='dashed')
plt.grid()
plt.legend(loc='upper right')
# to replace df positional index with weekdays
plt.xticks(df.index,['sun','mon','tue','wed','thu','fri','sat'])
plt.show()