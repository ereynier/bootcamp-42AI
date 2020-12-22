import numpy as np

def gradient(x, y , theta):
    M = x.shape[0]
    N = x.shape[1]
    X = np.concatenate((np.ones((M, 1)), x), axis=1)
    Xt = np.transpose(X)
    return((1. / M) * Xt.dot(X.dot(theta) - y))

x = np.array([
	      [ -6,  -7,  -9],
        [ 13,  -2,  14],
        [ -7,  14,  -1],
        [ -8,  -4,   6],
        [ -5,  -9,   6],
        [  1,  -5,  11],
        [  9, -11,   8]])
y = np.array([2, 14, -13, 5, 12, 4, -19])
theta1 = np.array([0,3,0.5,-6])

# Example :
print(gradient(x, y, theta1))

# Example :
theta2 = np.array([0,0,0,0])
print(gradient(x, y, theta2))