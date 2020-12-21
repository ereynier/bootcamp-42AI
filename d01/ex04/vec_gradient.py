import numpy as np
from tools import add_intercept

def gradient(x, y ,theta):
    M = x.shape[0]
    X = add_intercept(x)
    Xt = np.transpose(X)
    return((1. / M) * (Xt.dot((X.dot(theta)) - y)))


x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])

# Example 0:
theta1 = np.array([2, 0.7])
out = gradient(x, y, theta1)
print(out)

# Example 1:
theta2 = np.array([1, -0.4])
out = gradient(x, y, theta2)
print(out)