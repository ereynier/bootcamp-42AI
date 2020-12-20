import numpy as np
from tools import add_intercept


def predict_(x, theta):
    x = add_intercept(x)
    y_hat = np.dot(x, theta)
    return(y_hat)


x = np.arange(1,6)

# Example 1:
theta1 = np.array([5, 0])
out = predict_(x, theta1)
print(out)

# Example 2:
theta2 = np.array([0, 1])
out = predict_(x, theta2)
print(out)

# Example 3:
theta3 = np.array([5, 3])
out = predict_(x, theta3)
print(out)

# Example 4:
theta4 = np.array([-3, 1])
out = predict_(x, theta4)
print(out)