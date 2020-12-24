import numpy as np

def reg_cost_(y, y_hat, theta, lambda_):
    theta[0] = 0
    m = y.shape[0]
    return ((1. / (2 * m)) * (np.dot((y_hat - y), (y_hat - y)) + lambda_ * np.dot(theta, theta)))


y = np.array([2, 14, -13, 5, 12, 4, -19])
y_hat = np.array([3, 13, -11.5, 5, 11, 5, -20])
theta = np.array([1, 2.5, 1.5, -0.9])

# Example :
print(reg_cost_(y, y_hat, theta, .5))

# Example :
print(reg_cost_(y, y_hat, theta, .05))

# Example :
print(reg_cost_(y, y_hat, theta, .9))