import numpy as np
from sklearn.covariance import EmpiricalCovariance

x=np.array([[1,0,2],
            [0,1,1],
            [2,1,0],
            [1,1,1],
            [0,2,1]])
cov_est=EmpiricalCovariance().fit(x)
#in the above EmpiricalCovariance() creates an instance of class Empirical covariance.
#.fit(X) calculates the empirical covariance for x values
cov_mat=cov_est.covariance_
#.covariance_ converts it into a matrix
print(cov_mat)

mat=np.cov(x,rowvar=False,bias=True)
#here rowvar=False because our columns are features not rows
#we also give bias=True because sklearn empirical covariance considers the population covariance while
# numpy's .cov() considers sample covariance
print(mat)