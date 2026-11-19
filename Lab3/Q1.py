from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def load_data():
    data=pd.read_csv("~/Downloads/simulated_data_multiple_linear_regression_for_ML.csv")
    x=["age","BMI","BP","blood_sugar","Gender"]
    y=["disease_score"]
    return data[x],data[y]
def main():
    [x,y]=load_data()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=999)
    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train_scaled = scaler.transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    model = LinearRegression()
    model.fit(x_train_scaled, y_train)
    y_pred = model.predict(x_test_scaled)
    r2 = r2_score(y_test, y_pred)
    print(r2)
    print(y_pred)

if __name__ == "__main__":
     main()