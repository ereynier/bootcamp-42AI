import numpy as np

def zscore(x):
    return((x - np.mean(x)) / np.std(x))

# Example 1:
X = np.array([0, 15, -9, 7, 12, 3, -21])
print(zscore(X))

# Example 2:
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(zscore(Y))
