#Implement Gaussian PDF - mean = 0, sigma = 15 in the range[start=-100, stop=100, num=100]
import numpy as np
import math
x=np.linspace(-100,100,100)
sigma=15
mean=0
g=(1/sigma*(math.sqrt(2*math.pi)))*np.exp(-0.5*((x-mean)/sigma)**2)
print(g)