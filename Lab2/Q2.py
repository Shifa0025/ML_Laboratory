import numpy as np
a=np.array([2,1,2])
x=a.transpose()
print(x)
b=np.array([1,2,2])
y=b.transpose()
print(y)
dot_prod=x@y
print(dot_prod)
#dot product is the multiplication of each element of a matrix to the corresponding element in another matrix and summing their product.
#here 2*1=2,1*2=2,2*2=4 and 2+2+4=8,therefore the dot product is 8.