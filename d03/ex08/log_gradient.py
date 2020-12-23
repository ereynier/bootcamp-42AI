import numpy as np
from sigmoid import sigmoid_
from add_intercept import add_intercept


def log_gradient(x, y, theta):
    m = x.shape[0]
    if x.ndim == 1:
        n = 1
    else:
        n = x.shape[1]
    if theta.shape[0] != n + 1:
        print("theta have bad shape")
        return
    X = add_intercept(x)
    return ((1. / m) * np.dot(np.transpose(X),(sigmoid_(np.dot(X, theta)) - y)))


# Example 1:
y1 = np.array([1])
x1 = np.array([4])
theta1 = np.array([[2], [0.5]])

print(log_gradient(x1, y1, theta1))


# Example 2: 
y2 = np.array([[1], [0], [1], [0], [1]])
x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
theta2 = np.array([[2], [0.5]])

print(log_gradient(x2, y2, theta2))


# Example 3: 
y3 = np.array([[0], [1], [1]])
x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])

print(log_gradient(x3, y3, theta3))