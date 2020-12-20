import numpy as np

def cost_(y, y_hat):
    M = y.shape[0]
    if (y.size == 0 or y_hat.size == 0 or y.shape != y_hat.shape):
        print("Error on y or y_hat")
        return
    return (float(np.dot((y_hat - y), (y_hat - y)) / (2. * M)))