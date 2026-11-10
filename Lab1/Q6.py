#Implement y = 2x1 + 3x2 + 3x3 + 4, where x1, x2 and x3 are three independent variables. Compute the gradient of y at a few points and print the values.
import numpy as np
x1=np.linspace(-5,5,5)
x2=np.linspace(-2,2,5)
x3=np.linspace(-9,9,5)
y=2*x1+3*x2+3*x3+4
y1=2
y2=3
y3=3
print(y)
print("Gradient with respect to x1:",y1)
print("Gradient with respect to x2:",y2)
print("Gradient with respect to x3:",y3)