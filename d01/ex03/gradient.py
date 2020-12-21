import numpy as np
from prediction import predict_
from tools import add_intercept

def simple_gradient(x, y, theta):
    nab = np.ndarray((0,1))
    M = x.shape[0]
    y_hat = predict_(x, theta)
    nab = np.append(nab, [(1. / M) * np.sum(y_hat - y)])
    nab = np.append(nab, [(1. / M) * np.sum((y_hat - y) * x)])
    return(nab)


x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])

# Example 0:
theta1 = np.array([2, 0.7])
out = simple_gradient(x, y, theta1)
print(out)
lul(x, y, theta1)

# Example 1:
theta2 = np.array([1, -0.4])
out = simple_gradient(x, y, theta2)
print(out)