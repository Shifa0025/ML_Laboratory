import numpy as np
a=np.array([[1,2,3],
           [4,5,6]])
A=a.transpose()
print(A@a)
#multiplying a rectangular matrix with its transpose will give a square matrix

