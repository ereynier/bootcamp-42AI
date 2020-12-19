import numpy as np

def add_intercept(x):
    y = np.ones((x.shape[0], 1))
    if (x.ndim == 1):
        x = x.reshape((x.shape[0], 1))
    x = np.concatenate((y, x), axis=1)
    return x

x = np.arange(1,10).reshape((3,3))
y = add_intercept(x)
print(y)