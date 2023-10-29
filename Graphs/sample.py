import pandas as pd
import matplotlib.pyplot as plt
x=[2,3,4,5,6]
y=[100,400,600,50,700]
z=[300,500,600,530,800]
plt.plot(x,y,label='hcl')
plt.plot(x,z,label="hero")
plt.xlabel('data')
plt.ylabel('points')
plt.title('data vs points')
plt.grid()
plt.legend(loc='upper right')
plt.show()
