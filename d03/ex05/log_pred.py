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