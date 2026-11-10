#Implement y = 2x1 + 3 and plot x1, y [start=-100, stop=100, num=100]
import numpy as np
import matplotlib.pyplot as plt
x1=np.linspace(-100,100,100,dtype=int)
y= (2*x1)+3
plt.figure(figsize=(8,6))
plt.plot(x1,y,color='red',linewidth=2)
plt.show()
