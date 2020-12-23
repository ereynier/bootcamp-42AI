import numpy as np
from log_pred import logistic_predict_

def log_loss_(y, y_hat, eps=1e-18):
    y_hat = y_hat + eps
    m = y.shape[0]
    return ((-1. / m) * np.sum((y * np.log(y_hat)) + (1 - y) * np.log(1 - y_hat)))


# Example 1:
y1 = np.array([1])
x1 = np.array([4])
theta1 = np.array([[2], [0.5]])
y_hat1 = logistic_predict_(x1, theta1)
print(log_loss_(y1, y_hat1))


# Example 2:
y2 = np.array([[1], [0], [1], [0], [1]])
x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
theta2 = np.array([[2], [0.5]])
y_hat2 = logistic_predict_(x2, theta2)
print(log_loss_(y2, y_hat2))

# Example 3:
y3 = np.array([[0], [1], [1]])
x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
y_hat3 = logistic_predict_(x3, theta3)
print(log_loss_(y3, y_hat3))