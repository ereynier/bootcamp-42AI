import numpy as np
from  log_pred import logistic_predict_


#function need only numpy
def vec_log_loss_(y, y_hat, eps=1e-18):
    m = y.shape[0]
    y_hat = np.squeeze(y_hat)
    y = np.squeeze(y)
    if (y.shape != y_hat.shape):
        print("y and y_hat haven't same shapes")
        return
    y_hat = y_hat + eps
    ones = np.ones(m).squeeze()
    return ((-1. / m) * (np.dot(y, np.log(y_hat)) + np.dot((ones - y), np.log(ones - y_hat))))


y1 = np.array([1])
x1 = np.array([4])
theta1 = np.array([[2], [0.5]])
y_hat1 = logistic_predict_(x1, theta1)
print(vec_log_loss_(y1, y_hat1))

# Example 2:
y2 = np.array([[1], [0], [1], [0], [1]])
x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
theta2 = np.array([[2], [0.5]])
y_hat2 = logistic_predict_(x2, theta2)
print(vec_log_loss_(y2, y_hat2))

# Example 3:
y3 = np.array([[0], [1], [1]])
x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
y_hat3 = logistic_predict_(x3, theta3)
print(vec_log_loss_(y3, y_hat3))