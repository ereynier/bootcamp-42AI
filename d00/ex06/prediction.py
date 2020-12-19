import numpy as np
from tools import add_intercept

def predict_(x, theta):
    if (x.ndim != 1 or theta.ndim != 1 or theta.size != 2):
        print("x or theta haven't the good format")
        return
    X = add_intercept(x)
    return np.dot(X, theta)
