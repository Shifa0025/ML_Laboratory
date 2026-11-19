import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
def load_data():
    data=pd.read_csv("~/Downloads/simulated_data_multiple_linear_regression_for_ML.csv")
    x = ["age", "BMI", "BP", "blood_sugar", "Gender"]
    y = ["disease_score"]
    return data[x], data[y]


def data_split(x,y):
    n=int(0.7*len(x))
    tn=np.random.randint(0,60,n)
    x_train,y_train=x.iloc[tn],y.iloc[tn]
    x_test,y_test=x.drop(tn),y.drop(tn)
    return x_train,y_train,x_test,y_test


def hypothesis_test(x,theta):
    x1=x.to_numpy()
    x1 = np.hstack((np.ones((len(x1), 1)), x1))
    nrows=x1.shape[0]
    l=[]
    for i in range(nrows):
        a=x1[i].reshape(len(x1[i]),1)
        y=theta.T@a
        l.append(y)
    return l

def find_theta(x,y):
    x1=x.to_numpy()
    x1 = np.hstack((np.ones((len(x1), 1)), x1))
    y1=y.to_numpy()
    a=x1.T @ x1
    theta=np.linalg.inv(a) @ x1.T@y1
    return theta

def main():
    x,y=load_data()
    x_train,y_train,x_test,y_test=data_split(x,y)
    theta=find_theta(x_train,y_train)
    y_pred=hypothesis_test(x_test,theta)
    y_pred=[float(i[0][0]) for i in y_pred]
    r2=r2_score(y_test,y_pred)
    print(r2)

if __name__ == "__main__":
    main()