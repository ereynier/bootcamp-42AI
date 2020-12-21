import numpy as np
from tools import add_intercept


def predict_(x, theta):
    x = add_intercept(x)
    y_hat = np.dot(x, theta)
    return(y_hat)
