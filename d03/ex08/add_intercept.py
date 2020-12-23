import numpy as np

def add_intercept(x):
    X = np.ones((x.shape[0], 1), dtype=float)
    if (x.ndim == 1):
        x = x.reshape((x.shape[0], 1))
    X = np.concatenate((X, x), axis=1)
    return X