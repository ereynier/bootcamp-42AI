import numpy as np

def add_polynomial_features(x, power):
    x = x.reshape((x.shape[0], 1))
    tmp = x
    for i in range(2,power + 1):
        tmp = np.concatenate((tmp, x**i), axis=1)
    return (tmp)