import numpy as np

def minmax(x):
    return((x - np.min(x)) / (np.max(x) - np.min(x)))

# Example 1:
X = np.array([0, 15, -9, 7, 12, 3, -21])
print(minmax(X))

# Example 2:
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(minmax(Y))