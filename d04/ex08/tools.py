import numpy as np

def add_intercept(x):
    X = np.ones((x.shape[0], 1), dtype=float)
    if (x.ndim == 1):
        x = x.reshape((x.shape[0], 1))
    X = np.concatenate((X, x), axis=1)
    return X

def sigmoid_(x):
    return(1. / (1. + np.exp(-x)))

def predict_(x, theta):
    X = add_intercept(x)
    n = X.shape[1]
    if (theta.shape[0] != n):
        print("theta have bad shapes")
        return
    return (sigmoid_(np.dot(X, theta)))