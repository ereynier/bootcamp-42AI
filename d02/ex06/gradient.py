import numpy as np

def gradient(x, y , theta):
    M = x.shape[0]
    N = x.shape[1]
    X = np.concatenate((np.ones((M, 1)), x), axis=1)
    Xt = np.transpose(X)
    return((1. / M) * Xt.dot(X.dot(theta) - y))