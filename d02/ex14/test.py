import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mylinearregression import MyLinearRegression as MyLR
from polynomial_model import add_polynomial_features
from data_spliter import data_spliter


data = pd.read_csv("are_blue_pills_magic.csv")
x = np.array(data[["Micrograms"]])
y = np.array(data[["Score"]])

x_train, x_test, y_train, y_test = data_spliter(x, y, 0.5)

for i in range (2,6):
    x_train_poly = add_polynomial_features(x_train, i)
    my_lr = MyLR(np.full((i + 1), 10).reshape((-1, 1)), 50**-(i+3), i * 1600000)
    my_lr.fit_(x_train_poly, y_train)
    x_test_poly = x_test.reshape(-1,1)
    x_test_poly = x_test_poly[np.argsort(x_test_poly[:,0])]
    x_test_poly = add_polynomial_features(x_test_poly, i)
    y_hat = my_lr.predict_(x_test_poly)
    plt.scatter(x, y)
    '''plt.plot(x_test, y_hat, label=i)
    plt.legend(loc="best")'''
    cont = np.arange(1, 7, 0.01).reshape(-1,1)
    contp = add_polynomial_features(cont, i)
    y_hat = my_lr.predict_(contp)
    plt.plot(cont,y_hat)
plt.ylim(0, 100)
plt.show()