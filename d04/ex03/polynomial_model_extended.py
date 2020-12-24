import numpy as np

def add_polynomial_features(x, power):
    if (x.ndim == 1):
        x = x.reshape((x.shape[0], 1))
    n = x.shape[1]
    tmp = x
    for i in range(2,power + 1):
        for j in range(n):
            tmp = np.concatenate((tmp, np.array(x[:,j]**i).reshape((-1,1))), axis=1)
    return (tmp)


x = np.arange(1,11).reshape(5, 2)

# Example 1:
print(add_polynomial_features(x, 3))

# Example 2:
print(add_polynomial_features(x, 5))