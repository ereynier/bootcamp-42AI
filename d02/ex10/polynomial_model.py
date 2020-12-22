import numpy as np

def add_polynomial_features(x, power):
    x = x.reshape((x.shape[0], 1))
    tmp = x
    for i in range(2,power + 1):
        tmp = np.concatenate((tmp, x**i), axis=1)
    return (tmp)

x = np.arange(1,6).reshape(-1, 1)

# Example 1:
print(add_polynomial_features(x, 3))


# Example 2:
print(add_polynomial_features(x, 6))