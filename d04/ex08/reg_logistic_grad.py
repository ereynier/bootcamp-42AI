import numpy as np
from tools import add_intercept, predict_, sigmoid_

def reg_logistic_grad(y, x, theta, lambda_):
    m = y.shape[0]
    n = theta.shape[0]
    grad = np.ndarray((1,0))
    theta_prime = np.array(theta)
    theta_prime[0] = 0
    for j in range(n):
        J = 0
        for i in range(m):
            J += (sigmoid_(np.dot(np.insert(x, 0, 1, axis=1)[i], theta)) - y[i]) * np.insert(x, 0, 1, axis=1)[i][j] + lambda_ * theta_prime[j]
        grad = np.append(grad, (1 / m) * J)
    return(grad.reshape((-1,1)))



def vec_reg_logistic_grad(y, x, theta, lambda_):
    theta_prime = np.copy(theta)
    theta_prime[0] = 0
    m = y.shape[0]
    X = add_intercept(x)
    Xt = np.transpose(X)
    y_hat = predict_(x, theta)
    return ((1 / m) * (Xt.dot(y_hat - y) + lambda_ * theta_prime))


x = np.array([[0, 2, 3, 4], 
              [2, 4, 5, 5], 
              [1, 3, 2, 7]])
y = np.array([[0], [1], [1]])
theta = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])

# Example 1.1:
print(reg_logistic_grad(y, x, theta, 1))

# Example 1.2:
print(vec_reg_logistic_grad(y, x, theta, 1))

# Example 2.1:
print(reg_logistic_grad(y, x, theta, 0.5))

# Example 2.2:
print(vec_reg_logistic_grad(y, x, theta, 0.5))

# Example 3.1:
print(reg_logistic_grad(y, x, theta, 0.0))

# Example 3.2:
print(vec_reg_logistic_grad(y, x, theta, 0.0))
# Output: