import numpy as np
import math
x1=np.linspace(-10,10,100,dtype=int)
y=x1**2
print(y)
def derivative(x):
    y1=2*x
    return y1
print(derivative(-5))
print(derivative(-3))
print(derivative(0))
print(derivative(3))
print(derivative(5))

def x_value(y):
    x=math.sqrt(y)
    return x
print(x_value(0))
#Interpretation:the function reaches its global minima at x1=0
