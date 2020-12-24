import numpy as np

def reg_log_cost_(y, y_hat, theta, lambda_):
    m = y.shape[0]
    theta[0] = 0
    ones = np.ones((m, 1))
    ones = np.squeeze(ones)
    return((-1 / m) * (np.dot(y, np.log(y_hat)) + np.dot((ones - y), np.log(ones - y_hat))) + (lambda_ / (2 * m)) * np.dot(theta, theta))


y = np.array([1, 1, 0, 0, 1, 1, 0])
y_hat = np.array([.9, .79, .12, .04, .89, .93, .01])
theta = np.array([1, 2.5, 1.5, -0.9])

# Example :
print(reg_log_cost_(y, y_hat, theta, .5))

# Example :
print(reg_log_cost_(y, y_hat, theta, .05))

# Example :
print(reg_log_cost_(y, y_hat, theta, .9))