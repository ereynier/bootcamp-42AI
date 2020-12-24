import numpy as np
from tools import add_intercept, predict_


def reg_linear_grad(y, x, theta, lambda_):
    m = y.shape[0]
    n = theta.shape[0]
    grad = np.ndarray((1,0))
    theta_prime = np.array(theta)
    theta_prime[0] = 0
    for j in range(n):
        J = 0
        for i in range(m):
            J += (np.dot(np.insert(x, 0, 1, axis=1)[i], theta) - y[i]) * np.insert(x, 0, 1, axis=1)[i][j] + lambda_ * theta_prime[j]
        grad = np.append(grad, (1 / m) * J)
    return(grad.reshape((-1,1)))


def vec_reg_linear_grad(y, x, theta, lambda_):
    theta_prime = np.copy(theta)
    theta_prime[0] = 0
    m = y.shape[0]
    X = add_intercept(x)
    Xt = np.transpose(X)
    y_hat = predict_(x, theta)
    return ((1 / m) * (Xt.dot(y_hat - y) + lambda_ * theta_prime))
    


x = np.array([
      [ -6,  -7,  -9],
      [ 13,  -2,  14],
      [ -7,  14,  -1],
      [ -8,  -4,   6],
      [ -5,  -9,   6],
      [  1,  -5,  11],
      [  9, -11,   8]])
y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
theta = np.array([[7.01], [3.], [10.5], [-6.]])

# Example 1.1:
print("1.1")
print(reg_linear_grad(y, x, theta, 1))

# Example 1.2:
print("1.2")
print(vec_reg_linear_grad(y, x, theta, 1))

# Example 2.1:
print("2.1")
print(reg_linear_grad(y, x, theta, 0.5))

# Example 2.2:
print("2.2")
print(vec_reg_linear_grad(y, x, theta, 0.5))

# Example 3.1:
print("3.1")
print(reg_linear_grad(y, x, theta, 0.0))

# Example 3.2:
print("3.2")
print(vec_reg_linear_grad(y, x, theta, 0.0))