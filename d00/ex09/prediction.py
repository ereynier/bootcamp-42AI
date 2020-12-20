import numpy as np
from tools import add_intercept

def predict_(x, theta):
    X = add_intercept(x)
    return np.dot(X, theta)
