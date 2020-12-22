import numpy as np

class MyLinearRegression():
    def __init__(self, thetas, alpha=0.00001, n_cycle=100000):
        self.alpha = alpha
        self.n_cycle = n_cycle
        self.thetas = np.array(thetas)

    def add_intercept(self, x):
        X = np.ones((x.shape[0], 1), dtype=float)
        if (x.ndim == 1):
            x = x.reshape((x.shape[0], 1))
        X = np.concatenate((X, x), axis=1)
        return X

    def gradient(self, x, y):
        M = x.shape[0]
        X = self.add_intercept(x)
        Xt = np.transpose(X)
        return((1. / M) * (Xt.dot((X.dot(self.thetas)) - y)))

    def predict_(self, x):
        X = self.add_intercept(x)
        return (np.dot(X, self.thetas))

    def fit_(self, x, y):
        if (x.ndim == 1):
            x = x.reshape((x.shape[0]), 1)
            y = y.reshape((y.shape[0]), 1)
        self.thetas = self.thetas.reshape((self.thetas.shape[0], 1))
        for i in range(self.n_cycle):
            self.thetas = self.thetas - self.alpha * self.gradient(x, y)
        return (self.thetas)

    def cost_(self, x, y):
        M = y.shape[0]
        y_hat = np.squeeze(self.predict_(x))
        y = np.squeeze(y)
        if (y.size == 0 or y_hat.size == 0 or y.shape != y_hat.shape):
            print("Error on y or y_hat")
            return
        return (float(np.dot((y_hat - y), (y_hat - y)) / (2. * M)))

    def cost_elem_(self, x, y):
        y = y.reshape(y.shape[0], 1)
        y_hat = self.predict_(x)
        y_hat = y_hat.reshape(y_hat.shape[0], 1)
        M = y.shape[0]
        J_elem = np.zeros((M, 1))
        for i in range(M):
            J_elem[i][0] = (1. / (2. * M)) * (y_hat[i][0] - y[i][0])**2
        return J_elem

    def mse_(self, x, y):
        M = y.shape[0]
        return((1. / M) * np.sum((self.predict_(x) - y)**2))