import numpy as np
from tools import add_intercept

def gradient(x, y ,theta):
    M = x.shape[0]
    X = add_intercept(x)
    Xt = np.transpose(X)
    return((1. / M) * (Xt.dot((X.dot(theta)) - y)))