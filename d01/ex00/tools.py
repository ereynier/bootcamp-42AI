import numpy as np

def add_intercept(x):
    y = np.ones((x.shape[0], 1))
    if (x.ndim == 1):
        x = x.reshape((x.shape[0], 1))
    y = np.concatenate((y, x), axis=1)
    return y