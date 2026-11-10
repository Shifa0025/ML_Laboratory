#Implement y = 2x12 + 3x1 + 4 and plot x1, y in the range [start=--10, stop=10, num=100]
import numpy as np
import matplotlib.pyplot as plt
x1=np.linspace(-10,10,100)
y=(2*(x1**2))+(3*x1)+4
plt.figure(figsize=(8,5))
plt.plot(x1,y,color='red',linewidth=2)
plt.show()
