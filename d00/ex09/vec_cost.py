import numpy as np
from prediction import predict_

def cost_(y, y_hat):
    M = y.shape[0]
    if (y.size == 0 or y_hat.size == 0 or y.shape != y_hat.shape):
        print("Error on y or y_hat")
        return
    return (float(np.dot((y_hat - y), (y_hat - y)) / (2. * M)))

def cost_elem_(y, y_hat):
    y = y.reshape(y.shape[0], 1)
    y_hat = y_hat.reshape(y_hat.shape[0], 1)
    M = y.shape[0]
    J_elem = np.zeros((M, 1))
    for i in range(M):
        J_elem[i][0] = (1. / (2. * M)) * (y_hat[i][0] - y[i][0])**2
    return J_elem