import numpy as np
from tools import add_intercept

def predict_(x, theta):
    if (x.ndim != 1 or theta.ndim != 1 or theta.size != 2):
        print("x or theta haven't the good format")
        return
    X = add_intercept(x)
    return np.dot(X, theta)

x = np.arange(1,6)

theta1 = np.array((5, 0))
y = predict_(x, theta1)
print(y)

theta2 = np.array((0, 1))
y = predict_(x, theta2)
print(y)

theta3 = np.array([5, 3])
y = predict_(x, theta3)
print(y)

theta4 = np.array([-3, 1])
y = predict_(x, theta4)
print(y)