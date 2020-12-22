import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mylinearregression import MyLinearRegression as myLR
from polynomial_model import add_polynomial_features

data = pd.read_csv("are_blue_pills_magic.csv")
X = np.array(data[["Micrograms"]])
Y = np.array(data[["Score"]])

def comp_polynomial(X, Y, i):
    thetas = np.full((i + 1), 10).reshape((-1, 1))
    my_lr = myLR(thetas, 1e-7, 1000000)
    my_lr.fit_(X, Y)
    y_hat = my_lr.predict_(X)
    '''plt.scatter(np.transpose(X)[0], Y)
    plt.plot(np.transpose(X)[0], y_hat)
    plt.show()'''
    return (my_lr.cost_(X, Y))

cost = []
for i in range(2, 6):
    Xtmp = X
    if i > 1:
        Xtmp = add_polynomial_features(X, i)
    cost.append(comp_polynomial(Xtmp, Y, i))

x = np.arange(6 - 2)

plt.bar(x, cost)
plt.show()