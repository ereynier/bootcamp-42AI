import numpy as np
from sigmoid import sigmoid_
from add_intercept import add_intercept

def logistic_predict_(x, theta):
    X = add_intercept(x)
    n = X.shape[1]
    if (theta.shape[0] != n):
        print("theta have bad shapes")
        return
    return (sigmoid_(np.dot(X, theta)))

# Example 1
x = np.array([4])
theta = np.array([[2], [0.5]])
print(logistic_predict_(x, theta))

# Example 1
x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
theta2 = np.array([[2], [0.5]]) 
print(logistic_predict_(x2, theta2))

# Example 3
x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
print(logistic_predict_(x3, theta3))