import numpy as np

def predict_(x, theta):
    M = x.shape[0]
    N = x.shape[1]
    X = np.concatenate((np.ones((M, 1)), x), axis=1)
    return (np.dot(X, theta))

x = np.arange(1,13).reshape((4,3))

# Example 1:
theta1 = np.array([5, 0, 0, 0])
print(predict_(x, theta1))

# Example 2:
theta2 = np.array([0, 1, 0, 0])
print(predict_(x, theta2))

# Example 3:
theta3 = np.array([-1.5, 0.6, 2.3, 1.98])
print(predict_(x, theta3))

# Example 4:
theta4 = np.array([-3, 1, 2, 3.5])
print(predict_(x, theta4))