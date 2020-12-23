import numpy as np

class MyLogisticRegression():
    def __init__(self, thetas, alpha=0.001, n_cycle=100000):
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
        m = x.shape[0]
        if x.ndim == 1:
            n = 1
        else:
            n = x.shape[1]
        if self.thetas.shape[0] != n + 1:
            print("theta have bad shape")
            return
        X = self.add_intercept(x)
        return ((1. / m) * np.dot(np.transpose(X),(self.sigmoid_(np.dot(X, self.thetas)) - y)))

    def predict_(self, x):
        X = self.add_intercept(x)
        n = X.shape[1]
        if (self.thetas.shape[0] != n):
            print("theta have bad shapes")
            return
        return (self.sigmoid_(np.dot(X, self.thetas)))

    def fit_(self, x, y):
        if (x.ndim == 1):
            x = x.reshape((x.shape[0]), 1)
            y = y.reshape((y.shape[0]), 1)
        self.thetas = self.thetas.reshape((self.thetas.shape[0], 1))
        for i in range(self.n_cycle):
            self.thetas = self.thetas - self.alpha * self.gradient(x, y)
        return (self.thetas)

    def cost_(self, x, y, eps=1e-15):
        m = y.shape[0]
        y_hat = self.predict_(x)
        y_hat = y_hat - eps
        y_hat = np.squeeze(y_hat)
        y = np.squeeze(y)
        if (y.shape != y_hat.shape):
            print("y and y_hat haven't same shapes")
            return
        ones = np.ones(m).squeeze()
        return ((-1. / m) * (np.dot(y, np.log(y_hat)) + np.dot((ones - y), np.log(ones - y_hat))))

    def mse_(self, x, y):
        M = y.shape[0]
        return((1. / M) * np.sum((self.predict_(x) - y)**2))
    
    def minmax(self, x):
        return((x - np.min(x)) / (np.max(x) - np.min(x)))

    def zscore(self, x):
        return((x - np.mean(x)) / np.std(x))

    def sigmoid_(self, x):
        return(1. / (1. + np.exp(-x)))