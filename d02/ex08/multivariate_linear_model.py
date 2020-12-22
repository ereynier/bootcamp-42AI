import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mylinearregression import MyLinearRegression as myLR


def plot_(x, y, y_hat):
    plt.scatter(x,y, label="sell price")
    plt.scatter(x, y_hat, color="C9", s=10, label="predicted sell price")
    plt.legend(loc="best")
    plt.xlabel("x1")
    plt.ylabel("y")
    plt.grid()
    plt.show()

data = pd.read_csv("spacecraft_data.csv")
x1 = np.array(data["Age"])
x2 = np.array(data["Thrust_power"])
x3 = np.array(data["Terameters"])

'''
y = np.array(data["Sell_price"])
myLR_age = myLR([[800.], [-30.]], 0.001, 150000)
myLR_age.fit_(x1, y)
print(myLR_age.cost_(x1, y))
y_hat = myLR_age.predict_(x1)
plot_(x1, y ,y_hat)

myLR_thrust = myLR([[800.], [-30.]], 0.0001, 1500000)
myLR_thrust.fit_(x2, y)
print(myLR_thrust.cost_(x2, y))
y_hat = myLR_thrust.predict_(x2)
plot_(x2, y ,y_hat)

myLR_tera = myLR([[800.], [-30.]], 0.0001, 1500000)
myLR_tera.fit_(x3, y)
print(myLR_tera.cost_(x3, y))
y_hat = myLR_tera.predict_(x3)
plot_(x3, y ,y_hat)
'''



X = np.array(data[['Age', 'Thrust_power', 'Terameters']])
Y = np.array(data[['Sell_price']])
my_lreg = myLR([1.0, 1.0, 1.0, 1.0],  1e-5, 1500000)
print(my_lreg.cost_(X, Y))
my_lreg.fit_(X, Y)
print(my_lreg.cost_(X, Y))
y_hat = my_lreg.predict_(X)
plot_(x1, Y ,y_hat)
plot_(x2, Y ,y_hat)
plot_(x3, Y ,y_hat)