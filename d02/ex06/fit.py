import numpy as np
from gradient import gradient
from prediction import predict_

def fit_(x, y, theta, alpha, n_cycle):
    for i in range(n_cycle):
        grad = gradient(x, y, theta)
        theta = theta - alpha * grad
    return (theta)

x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta = np.array([[42.], [1.], [1.], [1.]])

# Example 0:
theta2 = fit_(x, y, theta,  alpha = 0.0005, n_cycle=42000)
print(theta2)

# Example 1:
print(predict_(x, theta2))
