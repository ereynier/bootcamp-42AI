import numpy as np

def predict_(x, theta):
    M = x.shape[0]
    N = x.shape[1]
    X = np.concatenate((np.ones((M, 1)), x), axis=1)
    return (np.dot(X, theta))